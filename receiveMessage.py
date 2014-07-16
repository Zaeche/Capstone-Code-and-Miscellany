#!/usr/bin/env python2.7

#Import from relevant header files and libraries
import serial
import string
import time, sys, datetime

#Specify the port to be opened
port = serial.Serial("/dev/ttyUSB0",9600)

#Open the serial port, send a message, then close the port
testArray = []

print('Reading message! Please stand by . . .\n')

print('To stop reading, press ctrl-C!')

while True:
	try:
		testArray.append(port.read())
	
	except KeyboardInterrupt:
		break
	
#End while loop

output = "" 
endval = len(testArray)
for i in range(0, endval):
	output += testArray[i] 

port.close()


bar_length = 40
for i in range (0, 101):
	percent = float(i)/100
	bars = ">"  * int(round(percent * bar_length))
	spaces = " " * (bar_length - len(bars))
	sys.stdout.write('\rReceiving message: [{0}] {1}%'.format(bars, int(round(percent*100))))
	sys.stdout.flush()
	time.sleep(0.025)
	
	if i == 100:
		sys.stdout.write("\n")

print(output)
