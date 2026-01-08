# Extensions

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

- sooner than `run_after_build__900_do_smth_else`
- later than `run_after_build__300_do_even_another_thing`



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

### FAQ

#### Can you give me examples of some extensions shipped in Armbian?

- [image-output-qcow2](https://github.com/armbian/build/blob/main/extensions/image-output-qcow2.sh): create images in qcow2-format, suitable to test-run in a VM.
- [uboot-btrfs](https://github.com/armbian/build/blob/main/extensions/uboot-btrfs.sh): Add btrfs support for u-boot
- [watchdog](https://github.com/armbian/build/blob/main/extensions/watchdog.sh): Add watchdog alert support

#### How to opt out of a specific hook function?

Any function making use of the extension framework [generally of the form `hook_name__individual_function`] can be skipped in a board or family config, by way of

```bash
extension_hook_opt_out "hook_name__individual_function"
```

Doing so is at the board/family maintainer's own risk and is officially unsupported. Consider splitting the function into pieces so that only the part the board/family cannot tolerate is skipped.
You can also opt out, then copy the otherwise-intolerable function into your own config and modify it as appropriate. Splitting the intolerable-function is still highly recommended.
