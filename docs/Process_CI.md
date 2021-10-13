# Automatic rebase of Pull requests

Pull most recent code from master branch and put your work on top within your pull request.

How to use it? Make a comment 

/rebase 

to trigger the action

- [Advantages of Git Rebase](https://itnext.io/advantages-of-git-rebase-af3b5f5448c6),
- [Automatic Rebase Action origin](https://github.com/marketplace/actions/automatic-rebase).

# Merge request pipelines

On each merge reqest we are running:

- shell script analysis
- creating Docker image
- building changed kernels

Those runs are for security reasons executed on public Github runners servers which are [very limited](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners#supported-runners-and-hardware-resources). One build cycle takes around one hour and it produces two types of artefacts:

- script anylysis report
- debian packages for kernel, device treee, headers, sources

Those build artefacts are available up to 14 days.

![Build](images/mr-pipeline.png)

<br>


<br>

## Build beta kernel packages 

<br>

Pipeline is extended version of merge requests pipeline. Pipeline is scheduled to run every day at 6am CET. It builds all changed kernels and update package repository in case it succeeds. 

What is affected by this pipeline?

- edge branch in stable repository https://apt.armbian.com
- all branches in beta repository https://beta.armbian.com

<br>
Trigger: every day at 6am CET
<br>
Condition: change in packages, upstream sources, patches or configuration

## Build all beta images

- triggered manually or uppon completion of nightly / edge builds;
- running the job manual is possible,
- pipeline is always using packages from https://beta.armbian.com repository.

<br>

## Build selected stable images
<br>
<br>

If you have a commit rights to the repository, go to [Armbian build system actions](https://github.com/armbian/build/actions) and select *Build selected*:

<br>

![Updating selected stable images](images/build-selected-blured.png)

You can recreate image(s) at main [download location](https://www.armbian.com/download/) from sources - set `packages from repository` to *no* - or from packages that are already in repository (default). In case you choose to build from sources, stable https://apt.armbian.com repository is going to be populated with newly created u-boot, kernel and **BSP packages for all boards** under (patched) stable version (yy.mm.**x+1**) which is incremented automatically if process succeeds.

![kanban screenshot](images/stable-images.png)

<br>

When new artifacts are created for stable builds, content is uploaded to CDN, then download and repository indexes are updated.  The process is typically complete in 1 to 2 days for major releases.
