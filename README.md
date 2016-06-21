# Intel-Edison-OS-Images
This repositories will feature binaries and tutorials on running debian, ubuntu, fedora and other operating systems on Intel Edison.

Detailed tutorials and binary releases will be placed here!

Published images may be burnt as follows


C:\Users\Bill\Documents\intel-edison\Distros\Alpine-Edison-Distro>flashall --recovery
Starting Recovery mode
Please plug and reboot the board
Flashing IFWI
Qt: Untested Windows version 6.2 detected!

XFSTK Downloader Solo 1.7.0
Copyright (c) 2014 Intel Corporation
Build date and time: Jul 10 2014 09:55:22

Intel SoC Device Detection Failed: Attempt #0
Intel SoC Device Detection Failed: Attempt #1
Intel SoC Device Detection Failed: Attempt #2
Intel SoC Device Detection Failed: Attempt #3
Intel SoC Device Detection Failed: Attempt #4
Intel SoC Device Detection Failed: Attempt #5
Intel SoC Device Detection Failed: Attempt #6
Intel SoC Device Detection Failed: Attempt #7
.Intel SoC Device Detection Found
Parsing Commandline....
Registering Status Callback....
.Initiating Download Process....
......................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................XFSTK-STATUS--Reconnecting to device - Attempt #1
..................XFSTK-STATUS--Reconnecting to device - Attempt #2
................................................................................................................................Recovery Success...
You can now try a regular flash

NOW IMMEDIATELY TYPE as BELOW

C:\Users\Bill\Documents\intel-edison\Distros\Alpine-Edison-Distro>flashall
Using U-boot target: edison-blankrndis
Now waiting for dfu device 8087:0a99
Please plug and reboot the board
Dfu device found
Flashing IFWI
Download        [=========================] 100%      4194304 bytes
Download done.
Download        [=========================] 100%      4194304 bytes
Download done.
Flashing U-Boot
Download        [=========================] 100%       237568 bytes
Download done.
Flashing U-Boot Environment
Download        [=========================] 100%        65536 bytes
Download done.
Flashing U-Boot Environment Backup
Download        [=========================] 100%        65536 bytes
Download done.
Rebooting to apply partiton changes
Dfu device found
Flashing rootfs, (it can take up to 5 minutes... Please be patient)
Download        [=========================] 100%    524288000 bytes
Download done.
Rebooting
U-boot & Kernel System Flash Success...
Your board needs to reboot to complete the flashing procedure, please do not unplug it for 2 minutes.

C:\Users\Bill\Documents\intel-edison\Distros\Alpine-Edison-Distro>
