#!/bin/sh


    # U-Boot.img map
    # 0x000000 - 0x001000 | padding with 0
    # 0x001000 - 0x200000 | u-boot0
    # 0x200000 - 0x300000 | primary environment
    # 0x300000 - 0x500000 | reserved
    # 0x500000 - 0x600000 | secondary environment

    # U-Boot.img on eMMC in LBA (LBA size: 512 bytes)
    #                     | description                | OSII | GPT label
    # 0x000000 - 0x000001 | MBR + OSIP                 | -    | -
    # 0x000001 - 0x000022 | GPT                        | -    | -
    # 0x000022 - 0x000800 | padding with 0 (alignment) | -    | -
    # 0x000800 - 0x001800 | u-boot0                    | 1    | u-boot0
    # 0x001800 - 0x002600 | primary environment        | -    | u-boot-env0
    # 0x002600 - 0x003600 | u-boot1                    | 2    | u-boot1
    # 0x003600 - 0x004400 | secondary environment      | -    | u-boot-env1


    # Fill U-Boot.img with 0
dd if=u-boot.img.no-osip bs=6M count=1
    # copy u-boot.bin in u-boot.img (u-boot0)
dd if=u-boot.bin of=u-boot.img.no-osip bs=1M conv=notrunc
    # copy (offset 2M) u-boot_env0.bin in u-boot.img (u-boot0)
dd if=env.bin of=u-boot.img.no-osip bs=1M conv=notrunc seek=2
    # copy (offset 5M) u-boot_env1.bin in u-boot.img (u-boot0)
dd if=env.bin of=u-boot.img.no-osip bs=1M conv=notrunc seek=5

