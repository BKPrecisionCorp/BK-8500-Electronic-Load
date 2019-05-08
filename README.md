# BK8500Examples

This project is a result of numerous customer support calls and is an effort to better help our customers solve their test challenges quickly and effectively. For questions not addressed here or for more details about the instrument see [B&K Precision](http://www.bkprecision.com)

## Command Interface
The command interface of the BK8500 series uses a 26 Byte packet interface. A command is a single packet and each command either returns a command status response packet or a command specific packet.

Basic usage:
import bk8500functions
create a list of 26 bytes - cmd=[0]*26
set the fields in the packet, the last of which is an 8-bit checksum - bk8500functions.csum(cmd) returns a checksum value.

### More Information
Go to the [8500 Series Page](https://www.bkprecision.com/products/dc-electronic-loads/8500-300-w-programmable-dc-electronic-load.html) for the user manual.

See the manual for details about specific commands.

Please submit a pull request or send a message to [technical support](https://www.bkprecision.com/support/contact-technician.html) to make changes.

## Organization

### Python
Within the Python folder there are examples of command sequences and a basic function library to simplify issuing commands.

#### bk8500functions.py
This is the "library". Extensions and improvements will likely happen here in the future. Today, this helps to create the 26-byte packet, calculate the checksum and print the returned values. Below is a typical example of using this set of functions. Normally the unit will be put into "remote" mode before any other command is issued.

```
import serial
import bk8500functions

ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM4'
print(ser)
ser.open()
print(ser.is_open)
#enable remote mode
cmd=[0]*26
cmd[0]=0xAA
cmd[2]=0x20
cmd[3]=1
cmd[25]=bk8500functions.csum(cmd)
bk8500functions.cmd8500(cmd, ser)
```

8500List.py uses bk8500functions.py and creates a list sequence in the load.

### LabView
Within the LabView folder, there are some basic examples as well. These are written using the LabView driver written by B&K for this product series. For these drivers, download the [8500 LabView Driver](https://www.bkprecision.com/products/dc-electronic-loads/8500-300-w-programmable-dc-electronic-load.html) located under the "Docs & Software" tab.

