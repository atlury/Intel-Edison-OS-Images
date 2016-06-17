def do_osip_mkimage():
    #
    # Stitch an image to create an OSIP image (OS Image Profile).
    # This script currently supports only one OSII (OS Image Identifier)
    # If more is necessary, it will need to be adjusted.
    #
    # This is the C struct for one OSII (size = 24 bytes)
    # struct OSII {                   //os image identifier
    #   uint16_t os_rev_minor;
    #   uint16_t os_rev_major;
    #   uint32_t logical_start_block; //units defined by get_block_size() if
    #                                 //reading/writing to/from nand, units of
    #                                 //512 bytes if cracking a stitched image
    #   uint32_t ddr_load_address;
    #   uint32_t entry_point;
    #   uint32_t size_of_os_image;    //units defined by get_page_size() if
    #                                 //reading/writing to/from nand, units of
    #                                 //512 bytes if cracking a stitched image
    #   uint8_t attribute;
    #   uint8_t reserved[3];
    # };

    # This is what a full OSIP header contains
    # Its size is 512 bytes
    # Offset   Size (bytes) Description
    # 0x000       4         OSIP Signature "$OS$"
    # 0x004       1         Reserved
    # 0x005       1         Header minor revision
    # 0x006       1         Header major revision
    # 0x007       1         Header checksum
    # 0x008       1         Number of pointers
    # 0x009       1         Number of images
    # 0x00a       2         Header size
    # 0x00c      20         Reserved
    # 0x020      24         1st bootable image descriptor (OSII)
    # 0x038      24         2nd bootable image descriptor (OSII)
    # ...       ...         ...
    # 0x170      24         15th bootable image descriptor (OSII)
    # 0x188      48         Not used
    # 0x1B8       4         Disk signature
    # 0x1BC       2         Null (0x0000)
    # 0x1BE      16         1st primary partition descriptor
    # 0x1CE      16         2nd primary partition descriptor
    # 0x1DE      16         3rd primary partition descriptor
    # 0x1EE      16         4th primary partition descriptor
    # 0x1FE       1         0x55
    # 0x1FF       1         0xaa

    import os
    import sys
    import argparse
    import struct

    # As only a small portion of the OSIP header needs to be changed
    # we simply store a full binary copy and we'll change just the
    # necessary values in it
    OSIP_HEADER_HEX_DATA = \
    '244f532400000121010138000000000000000000000000000000000000' \
    '00000000000000220000000000100100101001380100000f000000ffff' \
    'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff' \
    'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff' \
    'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff' \
    'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff' \
    'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff' \
    'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff' \
    'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff' \
    'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff' \
    'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff' \
    'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff' \
    'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff' \
    'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff' \
    'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff' \
    'ffffffffff00000000000000000000ee0000000100000000e0a3030000' \
    '0000000000000000000000000000000000000000000000000000000000' \
    '000000000000000000000000000000000055aa'

    def main():
        input_file = "u-boot.img.no-osip"
        output_file = "u-boot.img"
        handoff_pointer =  17829888
        destination_pointer = 17825792
        starting_lba = 2048

        in_file_data = open(input_file, 'rb').read()

        out_file = open(output_file, 'wb')

        # Write OSIP header data
        osip_header_data = bytearray(OSIP_HEADER_HEX_DATA.decode('hex'))

        # Override some values

        # Overrides starting LBA of imge in eMMC
        starting_lba_packed = struct.pack("I", starting_lba)
        osip_header_data[0x24:0x27+1]=starting_lba_packed

        # Overrides destination pointer to image in DDR
        destination_pointer_packed = struct.pack("I", destination_pointer)
        osip_header_data[0x28:0x2B+1]=destination_pointer_packed

        # Overrides pointer to handoff entry point in image
        handoff_pointer_packed = struct.pack("I", handoff_pointer)
        osip_header_data[0x2C:0x2F+1]=handoff_pointer_packed

        # The file needs to be padded to be multiple of 512 bytes

        # Overrides passed image size (in unit of 512 bytes blocks)
        padding_len_packed_block = struct.pack("I", ( (6*1024*1024) / 512))
        osip_header_data[0x30:0x33+1]=padding_len_packed_block

        # Compute XOR checksum
        osip_header_size = 1*0x18+0x20  # 24 bytes per OSII + 32 bytes header
        osip_header_data[0x07]=0
        crc = osip_header_data[0]
        for i in range(1, osip_header_size):
            crc ^= osip_header_data[i]
        osip_header_data[0x07]=crc

        out_file.write(osip_header_data)

        # Write image content
        out_file.write(in_file_data)

        out_file.close()

        return 0

    main()

do_osip_mkimage()

