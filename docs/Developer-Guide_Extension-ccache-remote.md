# Extension: ccache-remote

[ccache](https://ccache.dev/) significantly speeds up repeated kernel and
U-Boot builds by caching compiled objects. By default, each build host has
its own local cache. This extension adds a **shared remote cache** so that
multiple build machines (or a CI server and a developer workstation) can all
benefit from objects already compiled by someone else.

Typical scenarios:

- A home lab with several SBCs used as build hosts — first build populates
  the cache, subsequent builds on other machines hit it.
- A CI server and developer laptops sharing one cache server so that a
  developer rarely needs to compile from scratch after CI has run.
- A single machine where the local cache was lost (disk wiped) but the
  remote cache is still warm.

The extension supports two backends:

- **Redis** — lower latency, recommended for fast local networks. Cache lives
  entirely in RAM on the server, so capacity is limited by available memory.
- **HTTP/WebDAV** (nginx) — somewhat slower, but stores cache on disk. Can
  be orders of magnitude larger than a RAM-backed Redis instance, making it
  a better choice when cache size matters more than speed.

### Auto-discovery vs. explicit configuration

The simplest deployment uses **Avahi (DNS-SD)**. Once the cache server is
set up and publishing its service, and Avahi is installed on all build hosts,
enabling the extension is all that is needed — no URL configuration required.

If Avahi is not available or not desirable, the server URL must be provided
explicitly via `CCACHE_REMOTE_STORAGE`, or for remote servers via
`CCACHE_REMOTE_DOMAIN` (DNS SRV). See [Parameters](#parameters) below.

The extension automatically enables `USE_CCACHE=yes` and handles all ccache
configuration including Docker pass-through.

## Quick start

If a cache server is already running on the local network and advertising
itself via DNS-SD (Avahi), no configuration is needed:

```bash
./compile.sh BOARD=<board> BRANCH=<branch> ENABLE_EXTENSIONS="ccache-remote"
```

With an explicit Redis server:

```bash
./compile.sh BOARD=<board> BRANCH=<branch> \
  ENABLE_EXTENSIONS="ccache-remote" \
  CCACHE_REMOTE_STORAGE="redis://192.168.1.65:6379"
```

With an explicit HTTP/WebDAV server:

```bash
./compile.sh BOARD=<board> BRANCH=<branch> \
  ENABLE_EXTENSIONS="ccache-remote" \
  CCACHE_REMOTE_STORAGE="http://192.168.1.65:8088/ccache/"
```

To enable permanently from a userconfig file:

```bash
enable_extension "ccache-remote"
# optionally:
# CCACHE_REMOTE_STORAGE="redis://192.168.1.65:6379"
```

## Requirements

- **ccache**: version 4.4 or newer (for remote storage support).
- **Redis backend**: Redis server accessible from the build host.
- **HTTP backend**: nginx with WebDAV module (`nginx-extras`).
- **Auto-discovery**: `avahi-browse` (package `avahi-utils`) on the build host.

## Parameters

| Variable | Default | Description |
|---|---|---|
| **`CCACHE_REMOTE_STORAGE`** | _(empty)_ | Remote storage URL. If not set, auto-discovery is attempted. |
| **`CCACHE_REMOTE_DOMAIN`** | _(empty)_ | Domain for DNS SRV discovery (e.g. `example.com`). |
| **`CCACHE_REMOTE_ONLY`** | `no` | Set to `yes` to disable local cache and use only remote storage (saves local disk space). |
| **`CCACHE_REDIS_CONNECT_TIMEOUT`** | `500` | Redis connection timeout in milliseconds. |
| **`CCACHE_READONLY`** | _(empty)_ | Set to any value to use cache read-only (don't write new entries). |
| **`CCACHE_RECACHE`** | _(empty)_ | Recompile everything and update cache (bypass existing entries). |
| **`CCACHE_RESHARE`** | _(empty)_ | Push existing local cache entries to remote storage. |
| **`CCACHE_MAXSIZE`** | _(empty)_ | Maximum local cache size (e.g. `10G`). |
| **`CCACHE_NAMESPACE`** | _(empty)_ | Namespace for cache isolation between projects or branches. |
| **`CCACHE_DISABLE`** | _(empty)_ | Set to any value to disable ccache completely. |

For the full list of supported variables see the `CCACHE_PASSTHROUGH_VARS`
array in the extension source or the
[ccache configuration reference](https://ccache.dev/manual/latest.html#config_remote_storage).

### CCACHE_REMOTE_STORAGE URL format

```
Redis:  redis://[[USER:]PASSWORD@]HOST[:PORT][|attribute=value...]
HTTP:   http://HOST[:PORT]/PATH/[|attribute=value...]
```

Common attributes:

| Attribute | Default | Description |
|---|---|---|
| `connect-timeout` | `100` ms | Connection timeout. Increase on slow networks. |
| `operation-timeout` | `10000` ms | Per-operation timeout. |

Examples:

```
redis://192.168.1.65:6379|connect-timeout=500
redis://default:secretpass@192.168.1.65:6379|connect-timeout=500
http://192.168.1.65:8088/ccache/
```

!!! warning
    Redis passwords must not contain `/`, `+`, `=`, or spaces — these break
    URL parsing. Generate a safe password with:
    ```bash
    openssl rand -hex 24
    ```

## Server discovery

When `CCACHE_REMOTE_STORAGE` is not set, the extension tries to discover a
cache server automatically in this order:

1. **DNS-SD** (mDNS / Avahi): browse for `_ccache._tcp` on the local network.
   Requires `avahi-browse` on the build host and the cache server publishing
   a DNS-SD service. Redis is preferred over HTTP when both are found.

2. **DNS SRV**: query `_ccache._tcp.DOMAIN` when `CCACHE_REMOTE_DOMAIN` is
   set. Useful for remote or cloud-hosted build servers.

3. **Legacy mDNS**: resolve the hostname `ccache.local` (falls back to Redis
   on port 6379). Kept for backward compatibility.

If none of these succeeds, the extension silently falls back to local cache only.

## Cache sharing requirements

For the cache to be shared across multiple build hosts, **the Armbian source
tree must be at the same path on all machines** (e.g. `/home/build/armbian`).
ccache includes the working directory in the cache key, so different paths
produce different keys and the cache will not be shared.

Docker builds are not affected — they always use a consistent internal path.

## Server setup

### Redis (recommended)

1. Install:

    ```bash
    apt install redis-server avahi-daemon avahi-utils
    ```

2. Configure Redis — copy `misc/redis/redis-ccache.conf` from the extension
   directory and include it in `/etc/redis/redis.conf`:

    ```bash
    echo "include /etc/redis/redis-ccache.conf" >> /etc/redis/redis.conf
    systemctl restart redis-server
    ```

3. Set a password (recommended for any non-isolated network):

    ```bash
    openssl rand -hex 24   # use output as password
    # set requirepass <password> in redis-ccache.conf
    ```

4. Publish the DNS-SD service so clients discover it automatically:

    ```bash
    # Static (always advertise):
    cp misc/avahi/ccache-redis.service /etc/avahi/services/

    # Or tied to redis-server lifecycle:
    cp misc/systemd/ccache-avahi-redis.service /etc/systemd/system/
    systemctl enable --now ccache-avahi-redis
    ```

### HTTP/WebDAV (nginx)

1. Install:

    ```bash
    apt install nginx-extras avahi-daemon avahi-utils
    ```

2. Enable the WebDAV site:

    ```bash
    cp misc/nginx/ccache-webdav.conf /etc/nginx/sites-available/ccache-webdav
    ln -s /etc/nginx/sites-available/ccache-webdav /etc/nginx/sites-enabled/
    mkdir -p /var/cache/ccache-webdav/ccache
    chown -R www-data:www-data /var/cache/ccache-webdav
    systemctl reload nginx
    ```

3. Verify:

    ```bash
    curl -X PUT -d "test" http://localhost:8088/ccache/test.txt
    curl http://localhost:8088/ccache/test.txt
    ```

    !!! warning
        The provided nginx configuration has no authentication. Use only on a
        trusted private network.

4. Publish the DNS-SD service:

    ```bash
    cp misc/avahi/ccache-webdav.service /etc/avahi/services/
    ```

### DNS SRV records (remote servers)

For build hosts that cannot reach the cache server via mDNS, set
`CCACHE_REMOTE_DOMAIN` and create DNS records:

Redis backend:
```text
_ccache._tcp.example.com.  SRV  0 0 6379 ccache.example.com.
_ccache._tcp.example.com.  TXT  "type=redis"
```

HTTP/WebDAV backend:
```text
_ccache._tcp.example.com.  SRV  0 0 8088 ccache.example.com.
_ccache._tcp.example.com.  TXT  "type=http" "path=/ccache/"
```

### mDNS client requirements

For `.local` hostname resolution to work on the build host:

```bash
# Option A: systemd-resolved
apt install libnss-resolve

# Option B: standalone
apt install libnss-mdns
```

## References

- [ccache remote storage documentation](https://ccache.dev/manual/latest.html#config_remote_storage)
- [ccache Redis how-to](https://ccache.dev/howto/redis-storage.html)
- [ccache HTTP how-to](https://ccache.dev/howto/http-storage.html)
