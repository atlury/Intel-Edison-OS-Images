#!/bin/sh

    # U-Boot.bin map
    # 0x000000 - 0x001000 | padding with 0
    # 0x001000 - 0x200000 | u-boot0
dd if=/dev/zero of=u-boot.padding bs=4096 count=1
cat u-boot.padding u-boot.bin | dd of=u-boot.bin.padded

# Align u-boot.bin to 4K for dfu

filesize=$(stat -c %s u-boot.bin.padded)
alignment=$(echo "4096 - (${filesize} % 4096)" | bc)

if [ ${alignment} -ne 0 ];
    then
      dd if=/dev/zero of=u-boot.bin.padded bs=1 count=${alignment} conv=notrunc seek=${filesize}
fi

cp u-boot.bin.padded u-boot.bin

