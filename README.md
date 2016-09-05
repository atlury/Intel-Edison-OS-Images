# Intel-Edison-OS-Images

PLEASE REFER TO https://github.com/atlury/Intel-Edison-OS-Images/releases

This repositories will feature binaries and tutorials on running debian, ubuntu, fedora and other operating systems on Intel Edison. Detailed tutorials and binary releases will be placed here! Published images may be burnt as follows


flashall --recovery

It will say ..... .................Recovery Success...You can now try a regular flash

NOW IMMEDIATELY TYPE as BELOW

flashall

Your board needs to reboot to complete the flashing procedure, please do not unplug it for 2 minutes.

You are now ready

==For ubuntu 

Please edit /etc/network/interfaces and include your ssid and password within double quotes.

    wpa-ssid "ssid"
    wpa-psk "password"


Ap mode is also supported for Ubuntu

==Current Kernel is 4.8RC4 Mainline supporting the following
Wireless
External SD-Card
Internal MMC
SPI/I2C

==Working-in-progress (streamline)
SPI / DMA, PWM and intel_idle

==Not-yet-started/Unknown
No Audio, no BT, no PSHSST will supported for now.

==Mainline with devicetree will officially begin from 4.9
