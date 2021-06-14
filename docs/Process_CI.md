# Continuous integration

They are a combination of Github Actions scrips and scripts that run on our servers. Armbian is providing big number of turnkey binaries which builds are distributed over our build farm.

# Build pipelines

## Build 

- stable repository: EDGE kernels + board support packages are updated if there are any upstream sources, patches or config changes for EDGE kernels.
- beta repository:  all kernels + board support packages are updated if there are any upstream sources, patches or config changes
- rootfs cache: if some package in userland is changed, respective caches are recreated

Trigger: **every day at 6am CET**

In case any files are created in the process, they are uploaded to CDN, torrents recreated.

## Beta images

Trigger: right after build

All beta images are rebuild.

## Stable images

Trigger: manually

You can recreate image(s) from sources or from packages that are already in repository. In case you choose to build from sources, stable repository is getting 
populated with the u-boot, kernel and all newly created BSP packages under the version (21.10.x+1) which is read from a file in our internal repository. 
