import serial
import time
import sys
import packet

portSerialName = '/dev/ttyUSB0'
baudRateValue = 9600

try:
    ser = serial.Serial(
        port=portSerialName,
        baudrate=baudRateValue,
        parity=serial.PARITY_ODD,
        stopbits=serial.STOPBITS_TWO,
        bytesize=serial.SEVENBITS
        )
    ser.isOpen()
except serial.SerialException:
    print("Device not connected")
    
input = 0

while 1:
    
    msgData = raw_input("Enter data:(no more than 2 chars): ")[:2]
    msgType  = raw_input("Select message type:(0 - get,1 - set):")[:1]
    
    if (msgData == 'qt'):
        ser.close()
        exit()
    else:
        out = ''
        pkt = packet.packet()
        pkt.setType(msgType)
        pkt.setData(msgData)
        pkt.calculateCrc()

        stringToSend = pkt.packetToString()

        print stringToSend     
   
        ser.write(stringToSend)
        time.sleep(1)
        while (ser.inWaiting() > 0):
         out += ser.read(1)

        if (out != ''):
            print out
