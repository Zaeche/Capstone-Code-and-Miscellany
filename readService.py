#!/usr/bin/env python2.7

# Import from relevant header files and libraries
import serial, string, struct
import ctypes, os, mmap
import time, sys, datetime

# New empty map file:
file = os.open('/var/www/io_Data', os.O_CREAT | os.O_TRUNC | os.O_RDWR)

# Calibrate to correct size:
assert os.write(file, 2 * '\x00' * mmap.ALLOCATIONGRANULARITY) == 2 * mmap.ALLOCATIONGRANULARITY

# Create an MMAP instance:
dataExchange = mmap.mmap(file, mmap.PAGESIZE, mmap.MAP_SHARED, mmap.PROT_WRITE)

# The size of the message being received:
messageSize = 2

while True: 
	try:	
		# Specify the port to be opened
		serialPort = "/dev/ttyUSB0"
		port = serial.Serial(serialPort,9600)

		# Open the serial port, send the appropriate message
		#port.write('This is a test message -- do you read?')
	
		# Open port and listen for acknowledgement(s)
		testArray = []
		while len(testArray) < messageSize:
			try:
				testArray.append(port.read())
					
	        	except KeyboardInterrupt: 
				print('An unknown error has occurred with the readService!')
				break
		# End while loop
		port.close()
  
		# Go from an array to a string
		readData = ""
		endval = len(testArray)

		for i in range(0, endval): 
			readData += testArray[i]
				
		# Create an integer:
		i = ctypes.c_int.from_buffer(dataExchange)
		i.value = 10
		assert i.value == 10

		# Determine offsets and fix them:
		offset = struct.calcsize(i._type_)
		#assert dataExchange[offset] == '\x00'

		# Create a string
		s_type = ctypes.c_char * len(readData)
		s = s_type.from_buffer(dataExchange, offset)
		s.raw = readData
		
	except KeyboardInterrupt:
		print ('Error with readService!')
		break	

