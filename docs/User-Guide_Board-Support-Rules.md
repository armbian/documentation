# Support Definitions, Criteria and Relationships 

## Overview

Support statuses:

- Standard support
- Staging
- Community maintained

## Gold and Platinum Support

Gold and Platinum support is reserved for business relationships with the Armbian project and is out of the scope of this document. Please [contact us](https://www.armbian.com/contact/) for more information.

## Standard Support

### Benefits provided for a Standard Supported SBC

* Armbian will publish and distribute "stable" images through its [mirror network](https://github.com/armbian/mirror) (behind automated closest mirror selection)
* Armbian will publish and distribute "rolling" [images](https://github.com/armbian/os/releases/latest) (on GitHub and individual download page)
* best-effort support to SBC maintainer to assure compatiblity within the [Armbian Build Framework](https://github.com/armbian/build)
* best-effort team's unique expertise to assist maintainer with general challenges
* best-effort [automated testing](https://github.com/armbian/os#latest-smoke-tests-results) for basic hardware functionality
* best-effort compensation will be provided to maintainer from the "Armbian Community Fund" [[1]](https://github.com/sponsors/armbian) [[2]](https://liberapay.com/armbian) [[3]](https://forum.armbian.com/crowdfunding/)

### Criteria for Supported

For a SBC to be considered supported:

* must be beneficial to the Armbian project
* Armbian team must confirm and agree upon all supported boards statuses
* a named individual as "*maintainer*" with GitHub ID must be preset in the BOARD_MAINTAINER within [Board Configuration File](https://github.com/armbian/build/tree/main/config/boards)
* a named individual must commit to providing "*best effort*" support for their SBC on the Armbian forums
* maintainer must participate in the [Release Process](https://docs.armbian.com/Process_Release-Model/#release-coordinating)
* maintainer must sign-off that device has been tested, is stable, and ready for release during release process
* maintainer must have physical access to the SBC they are supporting
* maintainer can operate under pseudonym but must [reveal his identity](https://www.armbian.com/update-data/) to Armbian management
* maintainer should attend [developers meetings](https://forum.armbian.com/events/) held every Wednesday 7:00 PM CET
* when whole support burden is carried by maintainer of Armbian, it will be labelled as "Pro bono"

Additional Caveats:

* if the burden placed on the maintainer and Armbian team is too high, [crowdfunding campaign](https://forum.armbian.com/crowdfunding/) success will decide support
* supported is **not** applied to a "board family" or group of related SBCs. It is per board
* a maintainer can support multiple devices but must satisfy all requirements above per SBC
* any individual can be a maintainer for a standard support SBC
* missed major release will result in immediate forfeit of "Armbian Supported" status and demotion to CSC status unless Armbian team grants exemption

## Community maintained

Community maintained devices are not under active development and support status is unknown to Armbian team. It represents combined former CSC (community supported configuration) and EOS (end of support). Can be removed from Armbian code base at any time. Left as a courtesy in case a community member wants to attempt to resurrect development.

Community maintained SBCs are exclusively supported by the community.

### Caveats for Community maintained SBC

* Armbian will publish and distribute images through its [mirror network](https://github.com/armbian/mirror)
* Armbian will publish and distribute rolling [images](https://github.com/armbian/os/releases/latest) 
* periodic packages are built and published into Armbian's apt repository
* images are untested and Armbian team won't respond on troubles or apply any fixes.

### Requirements for Community Support

* patch or component does not break Armbian Build Framework
* patch or component does not break build of supported boards or other CSCs
* pull requests needs community review. Armbian team will not review any code related to community supported SBC
* generally considered to "work most of the time"
* generally considered to recieve periodic maintenance from community and upstream

## Staging - Work in progress

WIP status is for when a maintainer has commited to a SBC, but is not ready to ship stable images.

Benefits of Community Supported SBCs apply to WIP.

### Additional Benefits provided for a Staging status

* periodic / nightly CLI images are published by Armbian
* best-effort support to SBC maintainer to assure compatiblity within the [Armbian Build Framework](https://github.com/armbian/build)
* best-effort team's unique expertise to assist maintainer with general challenges
* eligible for promotion to Standard Support

### Criteria for WIP status

* must satisfy standard support criteria
* must show active development
