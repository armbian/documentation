# Build pipelines

<br>

They are a combination of Github Actions scrips and scripts that run on our servers. Armbian is providing big number of turnkey binaries which builds are distributed over our build farm.

<br>

## Nightly builds 

<br>

![Build](images/main-pipeline.png)

- edge branch in https://apt.armbian.com
- all branches in https://beta.armbian.com
- rootfs cache
<br>
In case new files are created, download and repository indexes are updated after content is uploaded to CDN which usually happens in 24 - 48h. With exception of beta repository, which update is instant.

<br>
<br>
Trigger: every day at 6am CET
<br>
Condition: changes in packages relations, upstream sources, patches or configurations

## Updating all beta images

<br>

![Updating all beta images](images/betaimages.png)

<br>

- triggered manually or automatically after nightly / edge build is finished,
- running the job manual is possible,
- pipeline is always using packages from https://beta.armbian.com repository.

<br>

## Updating selected stable images
<br>
<br>

If you have a commit rights to the repository, go to [Armbian build system actions](https://github.com/armbian/build/actions) and select *Build selected*:

<br>

![Updating selected stable images](images/build-selected-blured.png)

You can recreate image(s) from sources - set packages from repository to *no* - or from packages that are already in repository (default). In case you choose to build from sources, stable https://apt.armbian.com repository is going to be populated with newly created u-boot, kernel and **BSP packages for all boards** under (patched) stable version (yy.mm.**x+1**) which is incremented automatically if process succeeds.

![kanban screenshot](images/stable-images.png)

<br>

Download and repository indexes are updated after content is uploaded to CDN which usually happens in 24 - 48h. With exception of beta repository, which update is instant.
