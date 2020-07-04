# Release model

**Release Dates**

Armbian runs "train" based releases. Whatever is ready to board the train, does so. Whatever isn't ready, has to wait for the next train. This enables us to have a predictable release cycles making it easy to plan. It also puts the responsibility on developers to make sure they have features ready on time. 

Armbian releases quarterly at the end of **February, May, August, November**. Offset is because we all know that nothing happens for half of December. At the beginning of a release cycle, we have a planning meeting and **two weeks before the end of the release we freeze integration of new features**.

**Release Cycle**

Releases last 3 months. Each release starts with a planning meeting. After planning, developers and development teams build their deliverable using whatever methods (scrum, kanban, waterfall, ... ) they want but shall commit their code frequently, leading **up to the last 2 weeks**. The project does not accept "dumps" of code at the end. **Commit early and often** on master. Two weeks before the release date, we halt feature integration and only allow bug fixes. At some point during those two weeks, we start the release candidate process. This process starts by pulling a branch off master that will become the release branch. That frees up master for development on the next release. On the release candidate branch we work on bug fixes, and choose "release candidate", RC, tags. The software at that tag is a candidate for release, and it is submitted to automated and manual tests on real hardware. If automated tests are passing, we can officially tag it as the release. If it doesn't, we enter another bug fix cycle and create a new release candidate. We iterate until we have a candidate that can be the formal release. Usually, this takes 2-3 cycles and 1-3 weeks of time.

Development epics, stories and bugs for each release are tracked through [Jira](https://armbian.atlassian.net/).

# Release Branching, Versioning and Tags

Branches in Armbian follow this convention: 

 - **Master branch (master):** Main development will happen on the master branch. This is the latest and greatest branch, but is always "stable" and "deployable". All tests always pass on this branch.
 - **Maintenance branch (support):** This is the long-term maintenance branch per release.
 - **Development branch (dev)**: This is a branch created for lengthy and/or involved feature development that could destabilize master.

Each Armbian release will have the following version format:

**Format:** `<major>.<minor>.<revision>`

`<major>` and `<minor>` version will be incremented at the end of the release cycles while `<revision>` is incremented for a fix (or set of fixes)

Tags are used in ad-hoc manner.

# Release Naming

 
|version| codename | release month | work |
|:--|:--|:--|:--|
|19.11 | Vaquita| November| [done](https://armbian.atlassian.net/projects/AR/versions/10000/tab/release-report-all-issues)
|20.02 | Chiru| February| [done](https://armbian.atlassian.net/projects/AR/versions/10001/tab/release-report-all-issues)
| 20.05 | Kagu|May | [done](https://armbian.atlassian.net/projects/AR/versions/10002/tab/release-report-all-issues)
| 20.08 | Caple|August| [planned](https://armbian.atlassian.net/projects/AR/versions/10003/tab/release-report-all-issues)
| 20.11 |Tamandua|November|
 
 by http://www.codenamegenerator.com/

# Release Planning

A release planning starts with an public IRC meeting where developers and interested users come together in **first Saturday, one month before the release month**. 

Dates for **2020**: 

 * [April 4th](https://freenode.irclog.whitequark.org/armbian/2020-04-04)
 * July 4th 
 * October 3rd

Agenda:

- 00:00 - 00:02 Meeting coordinator (MC) calls meeting to order. 
- 00:02 - 00:05 MC gives control to participant to check-in and wait for latecomers. If your handle is not self explanatory, add your forum/github handle and just say hi.
- 00:05 - 00:07 MC [points out to agenda](https://github.com/armbian/documentation/blob/agenda/docs/Process_Release-Model.md#release-planning) and asks if there is any late topic to add.
- 00:07 - 00:09 MC presents meeting relevant news and rules of engagement:
  - news #1: IRC translator. If your English is poor, simply write in your native language. Start your sentence with .. at the beginning.
  - news #2: A document [how to use Jira](https://docs.armbian.com/Process_Managing_Workflow/)
  - rule #1: When you get a voice, be quick and concise (1-2 min) and make it clear when you stop. ("No more, I'm done")  
  - rule #2: If meeting is going out of desired agenda, MC will use "STOP STOP STOP", wait to get attention and then proceed with the meeting agenda. Please stop chatting and listen.
- 00:09 - 00:40 MC is calling out on by team sections as defined at GitHub: Allwinner, Amlogic, Marvell, Rockchip, others.
  - tasks should be [tracked by Jira](https://armbian.atlassian.net/secure/RapidBoard.jspa?rapidView=2). If they are not there, please add them during or right after the meeting
  - board Maintainers present tasks, bugs or projects they are working on (open discussion for each section if possible, otherwise MC calls people out).
  - [build script enhancements](https://armbian.atlassian.net/browse/AR-339?filter=10004)
  - [desktop and multimedia](https://armbian.atlassian.net/browse/AR-284?filter=10005)
- 00:40 - 00:50 [Cycle Jira backlog](https://armbian.atlassian.net/browse/AR) and:
   - discuss task / bug (one at a time)
   - assign to person / release / tag
   - re-prioritise
- 00:50 - 00:55 Cycle [open issues](https://github.com/armbian/build/issues) and [pull requests](https://github.com/armbian/build/pulls) on a build engine
- 00:55 - 00:56 Board status update on download pages and build engine (wip, supported, eol) https://www.armbian.com/download/
- 00:56 - 00:57 Choose upcoming release officer and next meeting organiser (1 or 2 roles). We need someone that is not well acquiented with the process to see if our documentation is good enough. He will get full support, so no need to worry about.
- 00:57 - misc / open discussion

Tips:

- channel is recorded so a summary and adjustments to Jira can made afterwards, ideally along with the meeting

Meeting location is IRC channel [#armbian](https://webchat.freenode.net/?channels=armbian) on [freenode](https://freenode.net/). Meeting starts **[at 2pm GMT](https://www.thetimezoneconverter.com/?t=14:00&tz=GMT)**.

# Release Coordinating

## Summary
A release starts as a RC Branch cut from master at freeze time.  Once a RC Branch is cut, master can be unfrozen and development can continue.  RC Branch is a rolling release that accepts bug fixes.  The bug fixes should be cherry-picked back to master branch.  Once the RC Is stable, A Final release as a branch named after its version.  A release is *never* merged to master.  Once a release is complete, it only should be updated for severe bugs and severe security vulnerabilities.  A release is only maintained until the next release.


## 1. Forum Communication

- Create a new thread in the [Armbian Build Framework Subforum](http://forum.armbian.com/forum/12-armbian-build-framework/)
  - Ex topic name: `Ambian 20.02 (Chiru) Release Thread`
- Tag the post with relase, release version, and codename
- Use the following template to begin the body of the release thread:

```
Release Candidate Code Freeze Date: YYYY-MM-DD
Release Date: YYYY-MM-DD
Release Candidate Branch Link: URL
Release Changelog: URL
Release Coordinator: @yourname
Testing Tracking Sheet: https://example.com/link  (google sheets)

The goal of this thread is to discuss testing, bugfixes, and the overall quality of the release.  Once the release is complete, this thread should be locked and unpinned. 
```
- Before Code Freeze --  Make note in the thread the incomplete jira issues tagged for the release [example](http://forum.armbian.com/topic/12763-armbian-2002-chiru-release-thread/?do=findComment&comment=93245)
- After test images are procuded, engage in community for assistants wih testing.. forums, twitter, etc.  [share this tool](http:///github.com/armbian/autotests)

## 2. Release Candidate Branch Management

- For code freeze -- create a RC branch as `version-rc` ex: `v20.02.0-rc`
- If Possible, create Jira tickets for major changes in github that were not tracked in Jira
- Begin Testing Process.  See [Release Testing](#Release_Testing)
- Do not modify branch directy.  Only accept PRs
- Only accept PRs for Bugfixes. No features
- Update master branch version to the NEXT release version with `-trunk`  ex. If RC is v20.02.0-rc Master bacomes v20.05.0-trunk
- CI Testing should pass on PR
- Test images should automatically be built via Igor's script
- Repeat build, test, and bugfix process until release is stable
- Cherry-pick bugfixes back into master
- Create Final Release branch from RC

## 3. Release

- In Github create a Release from final release branch
- Copy Release notes generated by Jira Release into Github form
- Add other appropriate information into release github release notes
- Point Armbian build system to new release
- Update armbian documentation to reflect current release
- Celebrate

# Release Testing

See [Opportunties for improvement](#Opportunities_for_Improvement)

# Reflection on Prior Releases
## Opportunities for Improvement

## wireless driver testing

* wireless is a particularly sensitive issue.  We need to test, fix, or at least be able to inform others of what is broken

### Bug Tracking



### Testing

### Image Downloads

## Positive Observations

* Good response from community for testing assistance
* Release was on time


# 
