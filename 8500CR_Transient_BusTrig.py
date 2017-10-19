#   8500List.py
#
#   Copyright {2017} {B&K Precision Corporation}

#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at

#       http://www.apache.org/licenses/LICENSE-2.0

#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
import serial
import bk8500functions
import time

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
#Set voltage limit
cmd=[0]*26
cmd[0]=0xAA
cmd[2]=0x22
cmd[3]=0x66
cmd[4]=0x3f
cmd[25]=bk8500functions.csum(cmd)
bk8500functions.cmd8500(cmd,ser)
#Set current limit
cmd=[0]*26
cmd[0]=0xAA
cmd[2]=0x24
cmd[3]=0xE0
cmd[4]=0x79
cmd[25]=bk8500functions.csum(cmd)
bk8500functions.cmd8500(cmd,ser)
#set power limit
cmd=[0]*26
cmd[0]=0xAA
cmd[2]=0x26
cmd[3]=0xCA
cmd[4]=0x41
cmd[5]=0x03
cmd[25]=bk8500functions.csum(cmd)
bk8500functions.cmd8500(cmd,ser)
#Read the model,serial,FW ver
cmd=[0]*26
cmd[0]=0xAA
cmd[2]=0x6A
cmd[25]=bk8500functions.csum(cmd)
bk8500functions.cmd8500(cmd,ser)
#set CR mode
cmd=[0]*26
cmd[0]=0xAA
cmd[2]=0x28
cmd[3]=0x3
cmd[25]=bk8500functions.csum(cmd)
bk8500functions.cmd8500(cmd,ser)
#set CR value
cmd=[0]*26
cmd[0]=0xAA
cmd[2]=0x30
cmd[3]=0xFF
cmd[4]=0xFF
cmd[5]=0x01
cmd[25]=bk8500functions.csum(cmd)
bk8500functions.cmd8500(cmd,ser)
#setup transient stuff
cmd=[0]*26
cmd[0]=0xAA
cmd[2]=0x38

cmd[3]=0xFF
cmd[4]=0xFF
cmd[5]=0x05
cmd[6]=0x00

cmd[7]=0x10
cmd[8]=0x1F

cmd[9]=0xFF
cmd[10]=0xFF
cmd[11]=0x01
cmd[12]=0x00

cmd[13]=0x10
cmd[14]=0x1F

cmd[15]=0x01
cmd[25]=bk8500functions.csum(cmd)
bk8500functions.cmd8500(cmd,ser)
#read the CR transient parameters back
cmd=[0]*26
cmd[0]=0xAA
cmd[2]=0x39
cmd[25]=bk8500functions.csum(cmd)
bk8500functions.cmd8500(cmd,ser)
#set trigger
cmd=[0]*26
cmd[0]=0xAA
cmd[2]=0x58
cmd[3]=0x02
cmd[25]=bk8500functions.csum(cmd)
bk8500functions.cmd8500(cmd,ser)
#Set mode to TRAN
cmd=[0]*26
cmd[0]=0xAA
cmd[2]=0x5D
cmd[3]=0x02
cmd[25]=bk8500functions.csum(cmd)
bk8500functions.cmd8500(cmd,ser)
#read input
cmd=[0]*26
cmd[0]=0xAA
cmd[2]=0x5F
cmd[25]=bk8500functions.csum(cmd)
bk8500functions.cmd8500(cmd,ser)
#enable input
cmd=[0]*26
cmd[0]=0xAA
cmd[2]=0x21
cmd[3]=0x01
cmd[25]=bk8500functions.csum(cmd)
bk8500functions.cmd8500(cmd,ser)
#delay so I can see it happen!
time.sleep(4)
#read input
cmd=[0]*26
cmd[0]=0xAA
cmd[2]=0x5F
cmd[25]=bk8500functions.csum(cmd)
bk8500functions.cmd8500(cmd,ser)
#trigger transient
cmd=[0]*26
cmd[0]=0xAA
cmd[2]=0x5A
cmd[25]=bk8500functions.csum(cmd)
bk8500functions.cmd8500(cmd,ser)
#delay so I can see it happen!
time.sleep(4)
#disable input
cmd=[0]*26
cmd[0]=0xAA
cmd[2]=0x21
cmd[3]=0x00
cmd[25]=bk8500functions.csum(cmd)
bk8500functions.cmd8500(cmd,ser)
#read trigger source
cmd=[0]*26
cmd[0]=0xAA
cmd[2]=0x59
cmd[3]=0x00
cmd[25]=bk8500functions.csum(cmd)
bk8500functions.cmd8500(cmd,ser)



ser.close()
