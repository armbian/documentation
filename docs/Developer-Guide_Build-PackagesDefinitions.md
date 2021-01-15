# Topic #

## Overview ##

This documentation should help you understand how to add :

* Debian distributions
* Desktop environments
* Application groups

And how to setup the list of packages to install and uninstall during
the image creation process.

## Level of support ##

Support levels can be anything you want, but an element is
considered supported if the level of support reads `supported`.

## Distributions names ##

All the distributions names are representend by folders inside
`config/distributions`.

## Debian distributions ##

To add a Debian distribution :
1. You have to create a folder inside `config/distributions/`.  
   The folder name should be the shortname of the distribution name,
   which will then be affected to `$RELEASE` during the build process.  
   We'll call this folder the **Distribution folder** in this procedure.
2. Inside the **Distribution folder**, create two files :
    * `name` must contain the full name of the distribution, as
      displayed in the selection menu (e.g. `Ubuntu Groovy 20.10` for
      `groovy`)
    * `support` must provide the **level of support** of the
       distribution.

The `RELEASE` environment variable correspond to a **Distribution folder**.

### Example 

For example, if you want to add the new distribution
`Doobian Humpty Hamster`, codenamed `hamster`, that you intend to support,
you'll have to create the following hierarchy in `config/distributions` :

```
hamster
+ name
+ support
```

* `config/distributions/hamster/name` should read `Doobian Humpty Hamster`
* `config/distributions/hamster/support` should read `supported`

## Common packages list directory architecture ##

The common directory architecture for desktop environments and applications
groups is :

* `packages`  
  A file containing the list of packages to install for this specific feature.
* `packages.remove`  
  A file containing the list of packages to filter out the list provided by
  `packages`.
* `packages.uninstall`  
  A file containing the list of packages to uninstall after installing
  everything, just before generating the image.
* `debian/postinst`
  Script executed after installing the Armbian Desktop meta-package. This
  is generally the last package installed.
* `armbian/create_desktop_package.sh`
  Script executed before generating the Armbian Desktop meta-package.
  Used to prepare files that can only be determined during the build phase.
* `sources/apt/*.source`
  The files in **sources/apt** are used to add Debian repositories, using
  `add-apt-repository`. Each file content is passed as an argument to
  `add-apt-repository -y -n "${source_file_content}"`, so the syntax follows
  anything you can pass to that command.
  * For each **source** file, you can also provide a corresponding GPG
    **key** file, which will be passed to `apt-key add`.  
    For example, if there's a file `sources/apt/docker.source` and a file
    `sources/apt/docker.key`, the `docker.source` file will be parsed to
    add an APT repository, while the `docker.key` will be passed to
    `apt-key add`.
* `only_for`
  Used to limit the selection and the use of the targeted option (desktop
  environment, appgroup, ...) to a specific list of architectures.  
  For example, if the file contains `arm64`, the option will only presented
  when building an image for an **arm64** board. Forcing the selection
  through environment variables will generate an error.  
  This is mainly used to limit options that make no sense for other
  architectures, due to a lack of packages for these architectures.

Each of this file is optional. Meaning that you only need to add them
if you need their functionnalities.

## Desktop environments ##

### Add a desktop environment to a distribution ###

Desktop environments are defined per distribution, in order to lower the
amount of corner cases to deal with when writing the packages lists, and the
various integration scripts.  
If a configuration is identical between two distributions, either create
a symlink or do a simple copy-paste of desktop environment folder.

Anyway, to create a desktop environment for a distribution (named
**RELEASE** here) :

1. Create a folder in `config/desktop/${RELEASE}/environments` with the
**codename** of the desktop environment you want to add (e.g. `gnome` for
the Gnome Desktop Environment). Avoid spaces inside the codename, replace
them by underscores if needed.

2. Inside this folder, add a `support` file that defined the **Level of support**
of the desktop environment.

> Only **supported** environments are displayed in the configuration menu,
when the `EXPERT` environment variable is not set to `yes`.

3. Add a least one configuration type, by creating a directory starting with
  `config_`. Then setup a
  **Common packages list directory architecture** inside it. What follows
  the `config_` prefix will be the shortname of the configuration
  presented to the user in the build configuration menus.  
  For example, if you define `config_base` and `config_full`, the user
  will be asked to choose between a `base` configuration and a `full`
  configuration after choosing that desktop environment.

4. For each configuration, you can provide board specific
  **packages list directory architecture**.  
  For this, create this **packages list directory architecture** inside
  a subdirectory `custom/boards/${BOARD}`.  
  For example, if you want to add specific packages for Nano PC T4 users,
  when building the **full** configuration of the `gnome` desktop environment,
  for Ubuntu `focal`, add them to :
  `config/desktop/focal/environments/gnome/config_full/custom/boards/nanopct4/packages`

> Actually, the directory for the desktop environment itself can contain a
**Common packages list directory architecture**. It's just that the build
configuration script is setup to search for configurations, so configurations
directories are still mandatory.  
However, that means that you can, for example, setup common packages files
for various configurations by putting a `packages` files inside the desktop
environment directory itself.

### Build an image using this desktop environment ###

Either :

* Start the build script and select the desktop environment during the
  configuration phase.

* Simply pass `DESKTOP_ENVIRONMENT="codename"` to the build script,
replacing `codename` by the codename of the desktop environment you
added (following the previous examples, you'd replace `codename` by
`gnome`).

> If you don't see the desktop environment you added,
  it generally means that you didn't define `EXPERT="yes"` and you
  also forgot to add a `support` file reading `supported` in the
  desktop environment directory.  

> Forcing the selection of an unsupported desktop environment, through
  `DESKTOP_ENVIRONMENT` while not an `EXPERT` will just lead to an
  error.


## Appgroups ##

Appgroups define a set of applications that a user can add by selecting
them in the build configuration menus.

### Add an appgroup ###

Appgroups are defined per distribution, referenced as `RELEASE` in the
various **bash** excerpts.

To add an appgroup :

* Create a directory in `config/desktop/${RELEASE}/appgroups` with the
**codename** of the appgroup as its name.

* Setup a **Common packages list directory architecture** inside this
directory.  
The most basic setup is to add a `packages` file containing the list of
packages to install when selecting this appgroup.

Once done, you can also add a :
* **board** specific **packages list directory architecture**
  inside a `custom/board/${BOARD}/` subdirectory.
* **destkop environment** specific
  **packages list directory architecture** inside a
  `custom/desktops/${DESKTOP_ENVIRONMENT}/` subdirectory.
* **board and desktop environment** specific
  **packages list directory architecture** inside a
  `custom/boards/${BOARD}/custom/desktops/${DESKTOP_ENVIRONMENT}/`
  subdirectory.


## CLI configurations ##

The new build system allows you to have different minimal
configurations, also called CLI configurations. These configurations
are basically limited to a set of packages, added after a debootstrap.

Only the packages files are supported in this configuration. Other
files (`only_for`, `debian/*`, `armbian/*`, `sources/*`, ...) are not
supported.

### Adding a CLI configuration ###

* Create a directory with the codename of the configuration, prefixed
  by `config_` inside `config/cli/${RELEASE}/main`.  
  For example, if you creating a `server` CLI configuration for Ubuntu
  `focal`, create the directory `config/cli/focal/main/config_server`.

* Add a `packages` file into this directory, containing the list of
  packages that should be installed when this configuration is chosen.
  You can also add `packages.uninstall` and `packages.remove` files too.

Once done, you can also add :
* **board** specific packages files inside a `custom/board/${BOARD}`
  subdirectory.

## Debootstrap configuration ##

You can also configure the debootstrap packages list. The customization
though is pretty limited.
The debootstrap configuration files for a specific distribution,
referenced as `RELEASE` are stored in
`config/cli/${RELEASE}/debootstrap`.

In this directory, the following files **need** to be added :

* `packages`  
  The list of packages to install during the debootstrap phase.
* `components`
  The list of components passed to the
  [debootstrap](https://linux.die.net/man/8/debootstrap) command.

You can also add :
* **CLI configuration specific** packages files and componennts
inside a `config_${SELECTED_CONFIGURATION}` subdirectory.
* **board** specific packages files and components inside a
`custom/board/${BOARD}` subdirectory.
* **CLI configuration and board specific** package files and
components inside a
`config_${SELECTED_CONFIGURATION}/custom/board/${BOARD}`
subdirectory.

