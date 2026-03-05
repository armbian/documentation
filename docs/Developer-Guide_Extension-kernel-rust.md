# Extension: kernel-rust

The Linux kernel has been gaining Rust support since version 6.1, with more
subsystems and drivers being written in Rust alongside traditional C code.
In the near future, practically useful drivers and subsystems for Armbian users
are expected to require or benefit from Rust kernel support. Enabling
`CONFIG_RUST` in the kernel build unlocks this capability.

Without this extension, Armbian kernels are built without Rust support —
the toolchain is not installed and `CONFIG_RUST` does not appear in
menuconfig. This extension installs a pinned Rust toolchain via `rustup`,
enables `CONFIG_RUST` automatically, and configures all required build
parameters so that Rust kernel modules can be compiled alongside C code.
The toolchain versions and other aspects of the build can be adjusted via
[parameters](#parameters) passed to the build system.

## Why rustup instead of distro packages

Distribution-provided Rust packages currently cannot fully satisfy all the
requirements for enabling Rust in a recent kernel. Mixing some components
from the distro with others from external sources is fragile and not
worthwhile. For this reason the extension downloads a complete, version-pinned
toolchain via `rustup` independently of the host distro.

When the base distro used by the Armbian build system provides packages
sufficient to build the Rust environment for the latest kernels entirely from
distro sources, Armbian will likely switch to using them.

## Quick start

```bash
./compile.sh BOARD=<board> BRANCH=<branch> ENABLE_EXTENSIONS="kernel-rust"
```

To open menuconfig with Rust options visible:

```bash
./compile.sh kernel-config BOARD=<board> BRANCH=<branch> ENABLE_EXTENSIONS="kernel-rust"
```

To enable permanently from a userconfig file:

```bash
enable_extension "kernel-rust"
```

## Requirements

- **Kernel version**: 6.12 or newer. The minimum required rustc version depends on the kernel release; see the [Rust-for-Linux version policy](https://rust-for-linux.com/rust-version-policy).
- **Host package**: `libclang-dev` — installed automatically by the extension.
- **Build host architecture**: x86_64, aarch64, or riscv64.
- Internet access on first use (downloads rustup-init and toolchain components).

## Parameters

| Variable | Default | Description |
|---|---|---|
| **`RUST_VERSION`** | `1.85.0` | rustc version installed via rustup. |
| **`BINDGEN_VERSION`** | `0.71.1` | `bindgen-cli` version installed via cargo. |
| **`RUST_KERNEL_SAMPLES`** | `no` | Set to `yes` to build sample Rust kernel modules (`rust_minimal`, `rust_print`, `rust_driver_faux`) as loadable modules. Useful for smoke-testing the toolchain. |
| **`RUST_EXTRA_COMPONENTS`** | _(empty array)_ | Additional rustup components to install (e.g. `clippy`, `llvm-tools`). |
| **`RUST_EXTRA_CARGO_CRATES`** | _(empty array)_ | Additional cargo crates to install. Supports `name` or `name@version` syntax. |

## Toolchain cache

The toolchain is installed once into `${SRC}/cache/tools/rustup/` and reused
across builds. The cache is content-addressed by a hash of:

- `RUST_VERSION`
- `BINDGEN_VERSION`
- build host architecture
- `RUST_EXTRA_COMPONENTS`
- `RUST_EXTRA_CARGO_CRATES`

Changing any of these values invalidates the cache and triggers a full reinstall
on the next build. The marker file is `.marker-<hash>` inside the cache directory.

## Extensibility

Other extensions can request additional toolchain components or crates before
the toolchain is installed:

```bash
# In your extension file:
RUST_EXTRA_COMPONENTS+=("clippy" "llvm-tools")
RUST_EXTRA_CARGO_CRATES+=("mdbook" "cargo-deb@2.11.0")
```

## Kernel artifact versioning

The extension adds a short hash of `RUST_VERSION|BINDGEN_VERSION` to the kernel
artifact version string (key `_R`, e.g. `rust1a2b`). This ensures that changing
toolchain versions triggers a kernel rebuild even if the kernel source is
unchanged.

## Implementation notes

### env -i isolation

The kernel build runs under `env -i`, which clears the entire environment.
The extension passes Rust tool paths directly as make parameters
(`RUSTC=`, `RUSTFMT=`, `BINDGEN=`) and sets `RUST_LIB_SRC` via the make
environment array. Direct paths into the toolchain sysroot are used instead
of rustup proxy binaries, so `RUSTUP_HOME` does not need to be in the
cleared environment.

### ccache and Rust

ccache does not support rustc (upstream won't-fix since 2019). The kernel
build system has no `RUSTC_WRAPPER` mechanism, so Rust compilation is not
cached by ccache. Only C/assembly compilation benefits from ccache when this
extension is active.

## References

- [Rust in the Linux kernel — quick start](https://docs.kernel.org/rust/quick-start.html)
- [Rust for Linux — version policy](https://rust-for-linux.com/rust-version-policy)
- [rustup installation](https://rust-lang.github.io/rustup/installation/index.html)
