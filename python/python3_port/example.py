import time
from dcload import DCLoad


def main():
    # Connecting to the load, setting it up and ramping up from 0 to 5A before shutting down again
    load = DCLoad("COM4", 9600, 0)  # Connecting to the load
    load.SetRemoteControl()  # Setting remote control
    load.TurnLoadOff()  # Making sure the load is off before setting up
    load.SetMode('cc')  # Setting CC mode
    load.SetMaxCurrent(10)  # Setting the maximum current
    load.SetMaxVoltage(100)   # Setting the maximum voltage
    load.SetMaxPower(300)  # Setting the maximum power
    load.SetCCCurrent(0)  # Setting the constant current setpoint
    load.TurnLoadOn()  # Enabling the load

    # Ramping up the current and printing parameters as we go
    for i in range(5):
        load.SetCCCurrent(i)
        time.sleep(0.5)
        print(load.GetInputValues())
        time.sleep(1)

    load.TurnLoadOff()  # Turning the load off
    load.SetLocalControl()  # Relinquishing remote control
    load.sp.close()  # Closing the serial port up

    # You can also connect to and use the load using a with statement
    with DCLoad("COM4", 9600, 0) as load:
        print(load.GetProductInformation())


if __name__ == "__main__":
    main()
