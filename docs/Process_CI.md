# Continuous integration

## Variants we use

1. Build

Trigger: cronjob at 6am CET

- stable repository: EDGE kernels + board support packages are updated if there are any upstream sources, patches or config changes for EDGE kernels.
- beta repository:  all kernels + board support packages are updated if there are any upstream sources, patches or config changes
- rootfs cache: if some package in userland is changed, respective caches are recreated

In case any files are created in the process, they are uploaded to CDN, torrents recreated.

2. Beta images

Trigger: right after build

All beta images are rebuild.

3. Stable images

Trigger: manually

You can recreate image(s) from sources or from packages that are already in repository. In case you choose to build from sources, stable repository is getting 
populated with the u-boot, kernel and all newly created BSP packages under the version (21.10.x+1) which is read from a file in our internal repository. 
