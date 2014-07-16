#!/usr/bin/env python2.7

#Import from relevant header files and libraries
import serial, string
import time, sys, datetime
import MySQLdb

#Specify the port to be opened
port = serial.Serial("/dev/ttyUSB0",9600)

try:
	#Open the serial port, send the appropriate message, then close the port
	if sys.argv[-1] == 'ON':
		data_1 = "Light One"
                data_2 = "ON"
                data_3 = "The light is now ON"
                data_4 = "N/a"
		
		port.write("0")
		#sys.stdout.write("Turning ON, please stand by.\n")
			
		try:
			db = MySQLdb.connect(host="localhost", user="testUser", passwd="tester", db="testDatabase")
			cur = db.cursor()

			cur.execute("""
				UPDATE statusTable
				SET State=%s, Description=%s, Temperature=%s
				WHERE Switch=%s
			""", (data_2, data_3, data_4, data_1))

			#cur.execute("INSERT INTO statusTable(Switch, State, Description, Temperature) VALUES('%s','%s', '%s','%s')" % (data_1, data_2, data_3, data_4))
	        	db.commit()
			
			cur.close()
			db.close()

		except:
			print("There seems to be a problem.")
			db.rollback()
	
	if sys.argv[-1] == 'OFF':
		data_1 = "Light One"
                data_2 = "OFF"
                data_3 = "The light is now OFF."
		data_4 = "N/A"
		
                port.write("1")
                #sys.stdout.write("Turning OFF, please stand by.\n")

                db = MySQLdb.connect(host="localhost", user="testUser", passwd="tester", db="testDatabase")
                cur = db.cursor()
		
	        cur.execute("""
                	UPDATE statusTable
                	SET State=%s, Description=%s, Temperature=%s
                	WHERE Switch=%s
                """, (data_2, data_3, data_4, data_1))

		# cur.execute("INSERT INTO statusTable(Switch, State, Description, Temperature) VALUES('%s','%s', '%s', '%s')" % (data_1, data_2, data_3, data_4))
                db.commit()

                cur.close()
                db.close()
	

#if sys.argv[-1] != 'OFF' or sys.argv[-1] != 'ON':
#	print('Error! Enter either ON or OFF, and try again.\n')
#	print(' Correct syntax is:\n \t\t"python sendMessage.py argValue" ')
#	print(' where argValue is either ON or OFF.')
#
except:
	print("Encountered an error!")

port.close()

#if sys.argv[-1] == 'ON' or sys.argv[-1] == 'OFF':
#
#	bar_length = 40
#	for i in range (0, 101):
#		percent = float(i)/100
#		bars = "|" * int(round(percent * bar_length))
#		spaces = " " * (bar_length - len(bars))
#		sys.stdout.write('\rPercentage Complete: [{0}] {1}%'.format(bars + spaces, int(round(percent*100))))
#		sys.stdout.flush()
#		time.sleep(0.025)
#		if i == 100:
#			sys.stdout.write("\n")

