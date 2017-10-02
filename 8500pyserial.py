#   8500pyserial.py
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

def cmd8500(cmd ):
    print("Command: ")
    printbuff(cmd)
    ser.write(cmd)
    resp = ser.read(26)
    print("Resp: ")
    printbuff(resp);
    
def printbuff(b):
    r=""
    for s in range(26):
        r+="|"
        r+=str(s)
        r+="-"
        r+=hex(b[s])
    print(r);

ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM3'
print(ser)
ser.open()
print(ser.is_open)
#enable remote mode
cmd8500([0xaa,00,0x20,0x01,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,0xcb])
cmd8500([0xaa,00,0x28,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,0xd2])
cmd8500([0xaa,00,0x21,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,0xcb])
cmd8500([0xaa,00,0x6a,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,0x14])
cmd8500([0xaa,00,0x28,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,0xd2])
cmd8500([0xaa,00,0x5d,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,0x07])
cmd8500([0xaa,00,0x2a,0xc8,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,0x9c])
cmd8500([0xaa,00,0x21,0x01,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,0xcc])
cmd8500([0xaa,00,0x5f,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,0x09])

ser.close()


