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
#Setup list operation
cmd=[0]*26
cmd[0]=0xAA
cmd[2]=0x3A
cmd[3]=0
cmd[25]=bk8500functions.csum(cmd)
bk8500functions.cmd8500(cmd, ser)
#read list operation
cmd=[0]*26
cmd[0]=0xAA
cmd[2]=0x3B
cmd[3]=0
cmd[25]=bk8500functions.csum(cmd)
bk8500functions.cmd8500(cmd, ser)
#set list repeat
cmd=[0]*26
cmd[0]=0xAA
cmd[2]=0x3c
cmd[3]=1
cmd[25]=bk8500functions.csum(cmd)
bk8500functions.cmd8500(cmd, ser)
#read list repeat
cmd=[0]*26
cmd[0]=0xAA
cmd[2]=0x3d
cmd[3]=0
cmd[25]=bk8500functions.csum(cmd)
bk8500functions.cmd8500(cmd, ser)
#set the number of steps
cmd=[0]*26
cmd[0]=0xAA
cmd[2]=0x3e
cmd[3]=4
cmd[4]=0
cmd[25]=bk8500functions.csum(cmd)
bk8500functions.cmd8500(cmd, ser)
#read the number of steps
cmd=[0]*26
cmd[0]=0xAA
cmd[2]=0x3f
cmd[3]=0
cmd[25]=bk8500functions.csum(cmd)
bk8500functions.cmd8500(cmd, ser)
#set a step!
cmd=[0]*26
cmd[0]=0xAA
cmd[2]=0x40
cmd[3]=1
cmd[5]=0xAA
cmd[9]=0xff
cmd[25]=bk8500functions.csum(cmd)
bk8500functions.cmd8500(cmd, ser)
#read that step
cmd=[0]*26
cmd[0]=0xAA
cmd[2]=0x41
cmd[3]=1
cmd[25]=bk8500functions.csum(cmd)
bk8500functions.cmd8500(cmd, ser)
#two more for fun!
#set a step!
cmd=[0]*26
cmd[0]=0xAA
cmd[2]=0x40
cmd[3]=2
cmd[5]=0xAA
cmd[9]=0xff
cmd[25]=bk8500functions.csum(cmd)
bk8500functions.cmd8500(cmd, ser)
#set a step!
cmd=[0]*26
cmd[0]=0xAA
cmd[2]=0x40
cmd[3]=2
cmd[5]=0xFF
cmd[9]=0x01
cmd[25]=bk8500functions.csum(cmd)
bk8500functions.cmd8500(cmd, ser)
#read that step
cmd=[0]*26
cmd[0]=0xAA
cmd[2]=0x41
cmd[3]=2
cmd[25]=bk8500functions.csum(cmd)
bk8500functions.cmd8500(cmd, ser)
###############
#Set the name
cmd=[0]*26
cmd[0]=0xAA
cmd[2]=0x48
cmd[3]=82
cmd[4]=121
cmd[25]=bk8500functions.csum(cmd)
bk8500functions.cmd8500(cmd, ser)
#read that name
cmd=[0]*26
cmd[0]=0xAA
cmd[2]=0x49
cmd[3]=0
cmd[25]=bk8500functions.csum(cmd)
bk8500functions.cmd8500(cmd, ser)

#save the list
cmd=[0]*26
cmd[0]=0xAA
cmd[2]=0x4C
cmd[3]=2
cmd[25]=bk8500functions.csum(cmd)
bk8500functions.cmd8500(cmd, ser)



ser.close()


