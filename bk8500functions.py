#   bk8500functions.py
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

def cmd8500(cmd , ser):
    print("Command: ", hex(cmd[2]))
    printbuff(cmd)
    ser.write(cmd)
    resp = ser.read(26)
    errorCheck(resp)
    #print("Resp: ")
    printbuff(resp);
    
def printbuff(b):
    r=""
    for s in range(26):
        r+=" "
        #r+=str(s)
        #r+="-"
        r+=hex(b[s]).replace('0x','')
    print(r);

def csum(thing):
    sum = 0;
    for i in range(len(thing)):
        sum+=thing[i]
    return 0xFF&sum;

def errorCheck(b):
    x = ""
    if b[3] == 0x90:
        print("Checksum Error: ", end='')
    elif b[3] == 0xA0:
        print("Parameter Incorrect: ",end='')
    elif b[3] == 0xB0:
        print("Unrecognized Command: ",end='')
    elif b[3] == 0xC0:
        print("Invalid Command: ",end='')
    elif b[3] == 0x80:
        print("Success: ",end='')
    else:
        print("Data return: ",end='')
