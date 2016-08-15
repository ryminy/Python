import time
import serial

#ser = serial.Serial('/dev/ttyUSB0', 9600) # Establish the connection on a specific port

def packetSend(data):
    out = ''
    portSerialName = '/dev/ttyUSB0'
    baudRateValue = 9600
    
    try:
        ser = serial.Serial(portSerialName,9600)

    except serial.SerialException:
      print("Device not connected")
      return "X"
    
    print("i am about to write ", data.decode());
    no = ser.write(data)
    print("%i bytes written on serial" % no)
    time.sleep(.2)

    out = ser.readline()
    ser.close()
    return out


while True:
     counter = input("please enter a char:")
     out = packetSend(counter.encode())
     print(out.decode())
    # ser.write(counter.encode()) # Convert the decimal number to ASCII then send it to the Arduino
     #print(ser.readline().decode()) # Read the newest output from the Arduino
     time.sleep(.1) # Delay for one tenth of a second

