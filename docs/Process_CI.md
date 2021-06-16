# Continuous integration

They are a combination of Github Actions scrips and scripts that run on our servers. Armbian is providing big number of turnkey binaries which builds are distributed over our build farm.

# Build pipelines

## Build 

![Build](images/nightly-edge-build.png)

- stable repository: EDGE kernels + board support packages are updated if there are any upstream sources, patches or config changes for EDGE kernels.
- beta repository:  all kernels + board support packages are updated if there are any upstream sources, patches or config changes
- rootfs cache: if some package in userland is changed, respective caches are recreated

Trigger: **every day at 6am CET**

In case any files are created in the process, they are uploaded to CDN, torrents recreated.

## Updating all beta images

![Updating all beta images](images/beta-images.png)

- triggered automatically after nightly / edge build is finished,
- running the job manual is possible,
- pipeline is always using packages from https://beta.armbian.com repository.

## Updating selected stable images

If you have a commit rights to the repository, go to [Armbian build system actions](https://github.com/armbian/build/actions) and select *Build selected*:

![Updating selected stable images](images/build-selected-blured.png)

You can recreate image(s) from sources - set packages from repository to *no* - or from packages that are already in repository (default). In case you choose to build from sources, stable https://apt.armbian.com repository is going to be populated with newly created u-boot, kernel and **BSP packages for all boards** under (patched) stable version (yy.mm.**x+1**) which is incremented automatically if process succeeds.

![kanban screenshot](images/stable-images.png)

Download and repository indexes are updated after content is uploaded to CDN which usually happens in 24 - 48h. With exception of beta repository, which update is instant.
