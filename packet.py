import time
import serial

        
def packetSendAndReceive(data):
    out = ''
    portSerialName = '/dev/ttyUSB0'
    baudRateValue = 9600
    
    try:
        ser = serial.Serial(portSerialName,9600)

    except serial.SerialException:
      print("Device not connected")
      return "X".encode()
    
    no = ser.write(data)
    print('am scris pe fir ' + str(no) + ' caractere') 
    time.sleep(1)

    out = ser.read()
    ser.close()
    return out









