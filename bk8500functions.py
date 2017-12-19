
def cmd8500(cmd , ser):
    print("Command: ", hex(cmd[2]))
    printbuff(cmd)
    ser.write(cmd)
    resp = ser.read(26)
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
