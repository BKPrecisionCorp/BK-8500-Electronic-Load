import serial
from dcload import DCLoad
import struct
import time

def main():
    load = DCLoad("COM4", 9600, 0)
    #load.Initialize()
    #test_struct = (struct.pack('BB', 0xaa, 0xbb))
    #test_struct = test_struct + test_struct
    #print(test_struct)

    load.SetRemoteControl()
    load.TurnLoadOff()
    load.SetMode('cc')
    load.SetMaxCurrent(10)
    load.SetMaxVoltage(100)
    load.SetMaxPower(300)
    load.SetCCCurrent(0)
    load.TurnLoadOn()
    #time.sleep(5)
    for i in range(5):
        load.SetCCCurrent(i)
        time.sleep(0.5)
        print(load.GetInputValues())
        time.sleep(1)

    load.TurnLoadOff()
    load.SetLocalControl()
    load.sp.close()

    with DCLoad("COM4", 9600, 0) as load:
        print(load.GetProductInformation())

    # ser = serial.Serial()
    # ser.baudrate = 9600
    # ser.port = 'COM4'
    # print(ser)
    # ser.open()
    # print(ser.is_open)
    # # enable remote mode
    # cmd = [0] * 26
    # cmd[0] = 0xAA
    # cmd[2] = 0x20
    # cmd[3] = 1
    # cmd[2] = bk8500functions.csum(cmd)
    # bk8500functions.cmd8500(cmd, ser)

if __name__ == "__main__":
    main()
