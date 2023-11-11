# Support Definitions, Criteria and Relationships 

## Overview

Support statuses:

1. Standard support
2. Staging
3. Community maintained

## Gold and Platinum Support

Gold and Platinum support is reserved for business relationships with the Armbian project and is out of the scope of this document. Please [contact us](https://www.armbian.com/contact/) for more information.

## Standard Supporte

### Benefits provided for a Standard Supported SBC

* Armbian will publish and distribute "stable" CLI images through its mirror network
* Armbian will publish and distribute "periodic / nightly" CLI and desktop images
* Armbian will work with SBC maintainer to assure compatiblity within the [Armbian Build System](https://github.com/armbian/build)
* Armbian will provide the team's unique expertise to assist maintainer with general challenges
* best-effort automated testing for basic hardware functionality
* best-effort compensation will be provided to maintainer from the "Armbian Community Fund"

### Criteria for Supported

For an SBC to be considered supported:

* must be beneficial to the Armbian project as a whole. In case support burden is carried by maintainer or Armbian, it has to be labelled as "Pro bono"
* Armbian team must confirm and agree upon all supported boards statuses
* a named individual as "*maintainer*" along with GitHub ID must be clearly identifed in the [Board Configuration File](https://github.com/armbian/build/tree/main/config)
* a named individual must commit to providing "*best effort*" support for their SBC on the Armbian forums
* maintainer must participate in the [Release Process](https://docs.armbian.com/Process_Release-Model/#release-coordinating)
* maintainer must sign-off that device has been tested, is stable, and ready for release during release process
* maintainer must have physical access to the SBC they are supporting 

Additional Caveats:

* If the burden placed on the Armbian team is too high funding maybe needed to assure:
    -  R&D bills paid. Failsafe in case Armbian members or a team was hired
    -  support bills covered by vendor or end users with crowdfunding campaign
* supported is **not** applied to a "board family" or group of related SBCs. It is per SBC
* a maintainer can support multiple devices but must satisfy all requirements above per SBC
* any individual can be a maintainer for a standard support SBC
* missed released will result in immediate forfeit of "Armbian Supported" status and demotion to CSC status unless Armbian team grants exemption

## Community maintained

Community maintained devices are not under active development and support status is uknown to Armbian team. It represent combined former CSC (community supported configuration) and EOS (end of support). Can be removed from Armbian code base at any time. Left as a courtesy in case a community member wants to attempt to resurrect development.

Community maintained SBCs are exclusively supported by the community.

### Caveats for Community maintained SBC

* periodic packages are built and published into Armbian's apt repository
* images are marked with "-unofficial" in the name
* images are untested

### Requirements for Community Support

* patch or component does not break Armbian Build Framework
* patch or component does not break build of supported or other CSCs
* pull requests needs community review. Armbian team will not review any code related to community supported SBC
* generally considered to "work most of the time"
* generally considered to recieve periodic maintenace from community and upstream

## Staging - Work in progress

WIP status is for when a maintainer has commited to a SBC, but is not ready to ship stable images.

Benefits of Community Supported SBCs apply to WIP.

### Additional Benefits provided for a Staging status

* periodic / nightly CLI images are published by Armbian
* Armbian will work with SBC maintainer to assure compatiblity within the [Armbian Build System](https://github.com/armbian/build)
* eligible for promotion to Standard Support

### Criteria for WIP status

* must satisfy standard support criteria
* must show active development
