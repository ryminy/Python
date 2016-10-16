import serial
import time

portSerialName = '/dev/ttyUSB0'
baudRateValue = 9600

def openSerial():
    try:
        ser = serial.Serial(portSerialName,baudRateValue)

    except serial.SerialException:
        print("Device not connected")
        return 'X'

    return ser

def closeSerial(ser):
    ser.close()

def readSerial(ser):
    return ser.readline()

def writeSerial(ser,data):
    return ser.write(data)
