# Release model

## Rolling releases

Armbian provides automated **daily** rolling releases for a [selected set of images](https://github.armbian.com/release-targets/targets-release-nightly.yaml) — the platinum-tier boards plus a manual selection, not every supported target. In addition, **community builds** are produced **weekly** for all [community-maintained boards](https://github.armbian.com/release-targets/targets-release-community-maintained.yaml).

Images are available on the respective board download pages: <https://www.armbian.com/download>. Armbian also populates its own package repository, so updates are available as an upgrade for existing installations.

## Point releases

Armbian runs "train"-based point releases: whatever is ready to board the train, does so; whatever is not has to wait for the next one. This makes for predictable, easy-to-plan release cycles, and puts the responsibility on developers to have their features ready on time.

Armbian releases quarterly, at the end of **February, May, August, and November** (the offset is because little happens over half of December).

## Release cycle

Development happens continuously on `main`, which is kept "stable" and "deployable" at all times — the project does not accept "dumps" of code at the end, so **commit early and often**.

The **release month** itself is spent **stabilizing the software stack**: feature integration winds down and the focus shifts to bug fixes and testing on real hardware across the supported boards. Once the stack is stable, the sources are frozen into a **release branch** and the release images are built and published.

Planning and coordination are not tied to a fixed schedule — they happen **ad hoc**: on [GitHub](https://github.com/armbian/build/issues) (issues, pull requests, release milestones), in the [forum](https://forum.armbian.com/), and in community meetings on [Discord](https://discord.com/invite/armbian), as work lands.

## Release branching, versioning and tags

Branches follow this convention:

- **Main branch (`main`)** — primary development. Always "stable" and "deployable"; all tests pass here.
- **Release branch (e.g. `v26.8`)** — one branch per release, with frozen external sources.

Each release uses the version format:

**`<major>.<minor>.<revision>`**

`<major>.<minor>` is the release **year and month** (e.g. `26.8` for August 2026); `<revision>` is incremented for a fix. Releases are identified by this version number — the animal codename scheme used through `26.2` has been retired. See [releases](/releases/) for the full history.

## Cutting a release

Once the software stack is stable, the release is cut from `main`:

1. Create the **release branch** and freeze its external sources:

    ```
    ./compile.sh targets
    cp output/info/git_sources.json config/sources/
    ```

    then commit the pinned sources to the build framework.
2. Tag a **GitHub release** from the release branch. Release notes are generated from the merged pull requests (see [releases](/releases/)); add any extra highlights.
3. Build and publish the release images, point the Armbian build system at the new release, and update the documentation.

A release branch is never merged back to `main`; after release it is maintained only for severe bugs and security vulnerabilities, and only until the next release.
