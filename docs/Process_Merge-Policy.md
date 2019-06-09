# Merge Policy #

## Overview ##
_Note: This document is a Work In Progress and is subject to change._

This policy is targeted for Maintainers for Lead Maintainers who have commit access to `master` branch.   This document describes the tags needed for different mege types.  See Definitions.

The types of code maintained fall into the following categories:

* Kernel
* U-Boot
* Build Scripts

Kernel and U-Boot maintainers are usually grouped by SoC Architecture.

Supported boards will have the most scrunity with code review.

## U-Boot Patches ##

- Standard Contributors provide _tested-by_ submitter (`armbianmonitor -u` with a fresh build)
- SoC maintainer maybe submit a PR with only a reviewed by of the lead SoC maintainer

## Kernel Related Patches ##

### default and next branches ###

- DT changes reviewed by at least one person familiar with this SoC (lead maintainer or deputy), _tested-by_ the contributor who sends it (armbianmonitor)..
- trivial module activation doesn't matter

### dev branches ###

Constraints are at the discretion of the SoC mantainer.   This builds are not expected to be stable.

## Armbian Build Scripts ##

This pertains to code used to build system images, OS configuration, and supporting packages.   (Basically Anything not U-Boot or Kernel source)

### lib scripts ###
* Requires at least one _Reviewed-by_

## Definitions ##

### Code Review Terms ###
#### Signed-off-by ####
Certifies that you wrote it or otherwise have the right to pass it on as a open-source patch.  

#### Acked-by ####

 If a person was not directly involved in the preparation or handling of a patch but wishes to signify and record their approval of it then they can arrange to have an Acked-by: line. Acked-by: does not necessarily indicate acknowledgement of the entire patch.  

#### Tested-by ####

A Tested-by: tag indicates that the patch has been successfully tested (in some environment) by the person named. This tag informs maintainers that some testing has been performed, provides a means to locate testers for future patches, and ensures credit for the testers.  

#### Reviewed-by ####

A Reviewed-by tag is a statement of opinion that the patch is an appropriate modification of the kernel without any remaining serious technical issues. Any interested reviewer (who has done the work) can offer a Reviewed-by tag for a patch. 

### Other ###

### Maintainer ###

An Individual designated to moderate, support and make decisions for a codebase or component.   There can be multiple maintainers assigned to any given thing.

### Lead Maintainer ###

A more experienced maintainer that will decide on high-impact and stategic changes and have final say in disputes.   A lead maintainer may share or designiate responsibility to some or all components within their domain of responsibility.

#### SoC ###

System on-a-Chip.
