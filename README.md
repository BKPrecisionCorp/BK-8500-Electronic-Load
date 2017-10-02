# BK8500Examples

This project is a result of numerous customer support calls and is an effort to better help our customers solver their test challenges quickly and effectively. For questions not addressed here or for more details about the instrument see www.bkprecision.com

#####################################

The command interface of the BK8500 series uses a 26 Byte packet interface. A command is a single packet and each command either returns a command status response packet or a command specific packet.

Basic usage:
import bk8500functions
create a list of 26 bytes - cmd=[0]*26
set the fields in the packet, the last of which is an 8-bit checksum - bk8500functions.csum(cmd) returns a checksum value.

#############################

The original author is learning Python at the moment, so please excuse poor coding style and rookie mistakes.
