# Armbian Task Management #

## Overview ##
TLDR; Keep task discussions in the forum. GitHub Issues are just for task metadata.

Tasks associated with code will have an issue created in GitHub, but **all dialog regarding tasks will reside on the forum** in a topic containing the github Issue ID of the task.

### What is a task? ###

A task is something actionable that results in some sort of tangible output. ex: code, documentation, QA findings.

Example sources of tasks include: feature requests, bugs, QA, general following of development roadmap.

Not all support issues are tasks, but a support issue can generate a task.


## Task Creation Procedure ##

1. Create issue in [Armbian GitHub Repo](https://github.com/igorpecovnik/lib/issues) under appropriate milestone
    - ![step1](images/taskProcess1.png)
1. Copy the numeric ID of issue created
1. Create new topic under the Tasks subforum on the [Armbian Forums](http://forum.armbian.com/index.php/forum/15-tasks/)
    - Use the the naming convention of `[ISSUE_ID] - Issue Name`
    - ![step2](images/taskProcess3.png)
1. Copy the URL of task subforum topic just created
1. Create comment on GitHub Issue with the following Content:
    -
    ```     
Please keep all discussion for this issue on the forum topic available below:

[URL](URL)
    ```
    - ![step4](images/taskProcess4.png)
1. Lock comments on GitHub Issue

## Task tracking with GitHub Issues ##

GitHub Issues provide an easy method to track and filter tasks by using tags and milestones.  Issues also make it easy to easily associate commits and merge requests with a task.  Effectively we just use GitHub issues for the metadata for reporting.

### Labels ###

Use labels identify the purpose of a task.


* `bug` is used to tag tasks that address Armbian-level bugs
* `not-our-bug` is used to identify tasks that are bugs in upstream code.  They are not Armbian bugs, but may impact Armbian.
* `enhancement` is used to identify tasks that are new features for Armbian.

### Milestones ###

Use milestones to divide tasks into claimed and unclaimed work.

* `claimed tasks` milestone contains tasks which have been assigned.
* `unclaimed tasks` milestone contains tasks that need an owner.


## Forum Tasks ##

### Converting a topic to a task ###

Sometimes support discussions can become tasks.   A forum admin can assist in moving the topic to Tasks forum group.  A cooresponding issue will need to be created.

## Future Process Improvements ##

Enhancements desired for this process \(This should be a task!\)

### Issue Hook ###

Ideally we can have a forum topic created upon issue creation.  This will save some time.
