## Armbian build system extensions framework (work in progress in #3300)

> "I'm gonna create a `prepare_bootloader` hook [in core] so we can refactor `u-boot` [into an extension]"


The extensions framework allows the board/family developers, extension authors, and users to extend the Armbian build system without overloading the core with specific functionality.

It's a simple framework, written in Bash, that **works based on function naming conventions**. It provides the core and the extensions with tracing and debugging, (error control,?) inline documentation and very simple dependency resolution.

### Terminology
- The "core" is everything that's in `lib/` directory plus `compile.sh` and some others. It's the spine of the build system.
- An "extension" is a separate Bash source file that contains exclusively functions. Extensions live in `extensions/` or `userpatches/extensions/` directory, but could one day be in a separate repository too.
- An "extension method" (a.k.a "hook") is used by the core to call extensions, via `call_extension_method()`. This will discover all enabled extension methods implementations, order them, and call them one by one.
    - The Armbian core already has quite a few of these in strategic spots.
    - More are coming as they're identified.
- An "extension method implementation" is a function that will be called when it's extension method is called. It can be defined in extensions, but also in board config, family config, user config, etc.

#### Example

##### Core calls extensions

The Armbian core build system has an extension method called `run_after_build`, also known as the "`run_after_build` hook". You can find it in `lib/main.sh` around line 546.

```bash
# in lib/main.sh:546
call_extension_method "run_after_build" [...]
```


##### Extension method implementation

Consider the following function:

```bash
function run_after_build__say_congratulations() { 
  echo "Congrats, the build is finished!"
}
```

Such a function is an "extension method implementation" called `say_congratulations` for the extension method `run_after_build`.

##### Extension file

A file `userpatches/extensions/be-festive.sh` containing the above function is an "extension" called `be-festive`.

##### Using it

An user of the build system can enable that extension by adding a call to `enable_extension "be-festive"` on his configuration file, or by passing `ENABLE_EXTENSIONS=be-festive` as a parameter to the build.


### Naming conventions and ordering

An extension method implementation is just a Bash function that follows the pattern `run_after_build__say_congratulations` where

- `run_after_build` is the name of the extension method.
- `__` is a marker/separator -- very important -- two underscores, not one, not three.
- `say_congratulations` is the name of the extension method implementation, and should be unique.

The system will "magically" compose a single `run_after_build()` function, based on all the hook functions that begin with `run_after_build__`.

Hook functions will be sorted by their numerical value; hook functions that do not begin with a number will receive `500_` prefix automatically.

So the examples `run_after_build__do_this` and `run_after_build__500_do_this` are equivalent, and will run

- sooner than `run_after_build_900_do_smth_else`
- later than `run_after_build_300_do_even_another_thing`



### What is an _extension_?

A extension is Bash source file that contains **exclusively**:

- function definitions:
    - extension method implementation definitions (with `__` separator)
    - other internal functions (for structure and clarity if needed)
- calls to `enable_extension "another-extension"` at the top of the file.
    - that's a very simple dependency system, one extension can enable another.

Specifically, **extension files should not contain any code outside of functions** -- they should do nothing when sourced.

Extensions can be official Armbian fragments and live in `/extensions`, or can be user-specific
in `/userpatches/extensions`.

An extension could be implemented in any of the following file/dir structures:

- `/extensions/our-ext.sh` - an official, single-file extension.
- `/userpatches/extensions/my-ext.sh` - a user-specific, single-file extension.
- `/extensions/our-dir-ext/our-dir-ext.sh` - an official, directory-based extension.
- `/userpatches/extensions/my-dir-ext/my-dir-ext.sh` - a user-specific, directory-based extensions.

The official extensions can be used by boards, family includes, etc, while the user-specific extensions can only be used by userpatches code or via `ENABLE_EXTENSIONS=my-ext,my-dir-ext` build parameter.

#### Single-file vs Directory-based

They're the same, except:

- Directory-based extensions will be passed a `${EXTENSION_DIR}` environment variable.
- That is useful if there are other files/assets that belong together with that extension. An example would be a template file, some configuration file, or other static asset that is directly related to the extension.
- Using directory-based extensions and `${EXTENSION_DIR}` allows for easy moving and PR'ing of user extensions.

## Hooks

- Hooks are listed in the order they are called.

### `post_family_config`

> *give the config a chance to override the family/arch defaults*

This hook is called after the family configuration (`sources/families/xxx.conf`) is sourced. Since the family can
override values from the user configuration and the board configuration, it is often used to in turn override those.

Also known as (for backwards compatibility only):

- `config_tweaks_post_family_config`

### `user_config`

> *Invoke function with user override*

Allows for overriding configuration values set anywhere else. It is called after sourcing the `lib.config` file if it
exists, but before assembling any package lists.

### `extension_prepare_config`

> *allow extensions to prepare their own config, after user config is done*

Implementors should preserve variable values pre-set, but can default values an/or validate them. This runs *after*
user_config. Don't change anything not coming from other variables or meant to be configured by the user.

### `post_aggregate_packages`

> *For final user override, using a function, after all aggregations are done*

Called after aggregating all package lists, before the end of `compilation.sh`. Packages will still be installed after
this is called, so it is the last chance to confirm or change any packages.

Also known as (for backwards compatibility only):

- `user_config_post_aggregate_packages`

### `post_determine_cthreads`

> *give config a chance modify CTHREADS programatically. A build server may work better with hyperthreads-1 for example.*

Called early, before any compilation work starts.

Also known as (for backwards compatibility only):

- `config_post_determine_cthreads`

### `add_host_dependencies`

> *run before installing host dependencies*

you can add packages to install, space separated, to ${EXTRA_BUILD_DEPS} here.

### `fetch_sources_tools`

> *fetch host-side sources needed for tools and build*

Run early to fetch_from_repo or otherwise obtain sources for needed tools.

### `build_host_tools`

> *build needed tools for the build, host-side*

After sources are fetched, build host-side tools needed for the build.

### `pre_install_distribution_specific`

> *give config a chance to act before install_distribution_specific*

Called after `create_rootfs_cache` (_prepare basic rootfs: unpack cache or create from scratch_) but
before `install_distribution_specific` (_install distribution and board specific applications_).

Also known as (for backwards compatibility only):

- `config_pre_install_distribution_specific`

### `pre_install_kernel_debs`

> *called before installing the Armbian-built kernel deb packages*

It is not too late to `unset KERNELSOURCE` here and avoid kernel install.

### `post_install_kernel_debs`

> *allow config to do more with the installed kernel/headers*

Called after packages, u-boot, kernel and headers installed in the chroot, but before the BSP is installed.
If `KERNELSOURCE` is (still?) unset after this, Armbian-built firmware will not be installed.

### `post_family_tweaks`

> *customize the tweaks made by $LINUXFAMILY-specific family_tweaks*

It is run after packages are installed in the rootfs, but before enabling additional services. It allows implementors
access to the rootfs (`${SDCARD}`) in its pristine state after packages are installed.

### `pre_customize_image`

> *run before customize-image.sh*

This hook is called after `customize-image-host.sh` is called, but before the overlay is mounted. It thus can be used
for the same purposes as `customize-image-host.sh`.

Also known as (for backwards compatibility only):

- `image_tweaks_pre_customize`

### `post_customize_image`

> *post customize-image.sh hook*

Run after the customize-image.sh script is run, and the overlay is unmounted.

Also known as (for backwards compatibility only):

- `image_tweaks_post_customize`

### `post_post_debootstrap_tweaks`

> *run after removing diversions and qemu with chroot unmounted*

Last chance to touch the `${SDCARD}` filesystem before it is copied to the final media. It is too late to run any
chrooted commands, since the supporting filesystems are already unmounted.

Also known as (for backwards compatibility only):

- `config_post_debootstrap_tweaks`

### `pre_prepare_partitions`

> *allow custom options for mkfs*

Good time to change stuff like mkfs opts, types etc.

Also known as (for backwards compatibility only):

- `prepare_partitions_custom`

### `prepare_image_size`

> *allow dynamically determining the size based on the $rootfs_size*

Called after `${rootfs_size}` is known, but before `${FIXED_IMAGE_SIZE}` is taken into account. A good spot to
determine `FIXED_IMAGE_SIZE` based on `rootfs_size`. UEFISIZE can be set to 0 for no UEFI partition, or to a size in MiB
to include one. Last chance to set `USE_HOOK_FOR_PARTITION`=yes and then implement create_partition_table hook_point.

Also known as (for backwards compatibility only):

- `config_prepare_image_size`

### `post_create_partitions`

> *called after all partitions are created, but not yet formatted*

### `format_partitions`

> *if you created your own partitions, this would be a good time to format them*

The loop device is mounted, so ${LOOP}p1 is it's first partition etc.

### `pre_update_initramfs`

> *allow config to hack into the initramfs create process*

Called after rsync has synced both `/root` and `/root` on the target, but before calling `update_initramfs`.

Also known as (for backwards compatibility only):

- `config_pre_update_initramfs`

### `pre_umount_final_image`

> *allow config to hack into the image before the unmount*

Called before unmounting both `/root` and `/boot`.

Also known as (for backwards compatibility only):

- `config_pre_umount_final_image`

### `post_umount_final_image`

> *allow config to hack into the image after the unmount*

Called after unmounting both `/root` and `/boot`.

Also known as (for backwards compatibility only):

- `config_post_umount_final_image`

### `post_build_image`

> *custom post build hook*

Called after the final .img file is built, before it is (possibly) written to an SD writer.

- *NOTE*: this hook used to take an argument ($1) for the final image produced.
    - Now it is passed as an environment variable `${FINAL_IMAGE_FILE}`
      It is the last possible chance to modify `$CARD_DEVICE`.

### `run_after_build`

> *hook for function to run after build, i.e. to change owner of `$SRC`*

Really one of the last hooks ever called. The build has ended. Congratulations.

- *NOTE:* this will run only if there were no errors during build process.

### `extension_metadata_ready`

> *meta-Meta time!*

Implement this hook to work with/on the meta-data made available by the extension manager. Interesting stuff to process:

- `"${EXTENSION_MANAGER_TMP_DIR}/hook_point_calls.txt"` contains a list of all hook points called, in order.
- For each hook_point in the list, more files will have metadata about that hook point.
    - `${EXTENSION_MANAGER_TMP_DIR}/hook_point.orig.md` contains the hook documentation at the call site (inline docs),
      hopefully in Markdown format.
    - `${EXTENSION_MANAGER_TMP_DIR}/hook_point.compat` contains the compatibility names for the hooks.
    - `${EXTENSION_MANAGER_TMP_DIR}/hook_point.exports` contains _exported_ environment variables.
    - `${EXTENSION_MANAGER_TMP_DIR}/hook_point.vars` contains _all_ environment variables.
- `${defined_hook_point_functions}` is a map of _all_ the defined hook point functions and their extension information.
- `${hook_point_function_trace_sources}` is a map of all the hook point functions _that were really called during the
  build_ and their BASH_SOURCE information.
- `${hook_point_function_trace_lines}` is the same, but BASH_LINENO info. After this hook is done,
  the `${EXTENSION_MANAGER_TMP_DIR}` will be removed.


