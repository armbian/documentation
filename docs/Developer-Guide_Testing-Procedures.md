It is important for tests to be performed in a consistent manner.
The purpose of formalized testing procedures is to provide a proven, reproducible process for verifying device compatibility and various features within Armbian.
The overall goal is to reduce variance in testing methodologies between individual contributors while enstilling confidence within new contributors and encouraging them to perform quality bug reports and ideally a pull/merge request.

## Hardware: Micro SD card

1. Insert the micro SD card **directly** into the corresponding port on the target device, if possible.
If intermediate hardware such as a microSD/USB adapter is used and the card is not detected, please include details of the adapter within the test results
Verify that the card is recognized in ``lsblk``
2. Verify that the card is recognized by a file manager
(If a device is ejected within the file manager, you may have to physically re-insert the card for it to appear again.)
3. Verify that the card can be mounted within a file manager
4. Navigate to the root directory of the card within a file manager.
Verify that the maximum storage capacity indicated is appropriate given the storage marked on the card
5. Verify that a non-empty text file can be written to the card
6. Verify that existing files may be read on the card
7. Using a N-GB card, verify that checksum evaluations pass if approximately N * 1 GB files are written to the card
