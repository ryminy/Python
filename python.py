import serial
import time

portSerialName = '/dev/ttyUSB0'
baudRateValue = 9600

ser = serial.Serial(
    port=portSerialName,
    baudrate=baudRateValue,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
    )

ser.isOpen()
input = 0

while 1:
    print('Waiting commands:')
    input = raw_input()
    if input == 'exit':
        ser.close()
        exit()
    else:
        out = ''
        ser.write(input)
        time.sleep(1)
        while ser.inWaiting() > 0:
            out += ser.read(1)

        if out != '':
            print(out)
            
    
