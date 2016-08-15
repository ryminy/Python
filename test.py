from time import sleep
import serial

ser = serial.Serial('/dev/ttyUSB1', 9600) # Establish the connection on a specific port


while True:
     counter = input("please enter a char:")
     ser.write(counter.encode()) # Convert the decimal number to ASCII then send it to the Arduino
     print(ser.readline().decode()) # Read the newest output from the Arduino
     sleep(.1) # Delay for one tenth of a second

