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
    input = raw_input("Enter data:(no more than 2 chars): ")[:2]
    if (input == 'qt'):
        ser.close()
        exit()
    else:
        out = ''
        pkt = packet.packet('1',input)
        pkt.calculateCrc()

        stringToSend = pkt.packetToString()

        print stringToSend
        ser.write(stringToSend)
        time.sleep(1)
        while ser.inWaiting() > 0:
         out += ser.read(1)

        if (out != ''):
            print(out)
