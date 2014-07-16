#!/usr/bin/env python2.7

# Import from relevant header files and libraries
import serial, string
import time, sys, datetime
import MySQLdb

# Specify the port to be opened
serialPort = "/dev/ttyUSB0"
port = serial.Serial(serialPort,9600)

# Open the serial port, send the appropriate message
port.write('This is a test message -- do you read?')

# Open port and listen for acknowledgement(s)
testArray = []
while len(testArray) < 16:
        try:
                testArray.append(port.read())

        except KeyboardInterrupt:
                break
# End while loop
port.close()

# The next step is to write the received data to the server. To this end, we do the following:
# Connect to the relevant database:
db = MySQLdb.connect(host="localhost", user="testUser", passwd="tester", db="testDatabase")

# Create a cursor object to execute queries
cur = db.cursor()

# Insert received data into the table  
# Go from an array to a string
data_1 = " "
data_2 = " " 
data_3 = " " 
endval = len(testArray)
for i in range(0, 4):
        data_1 += testArray[i]
for i in range (4, 5):
	data_2 += testArray[i]
for i in range (5, endval):
	data_3 += testArray[i]
# print data_1, data_2, data_3

try:
	cur.execute("INSERT INTO fromSwitch(Switch, Instruction, Data) VALUES('%s','%s', '%s')" % (data_1, data_2, data_3))
	db.commit()
except:
	print 'Error! Try again later.' 
	db.rollback()

# Select all the data from the table and print it out.
#cur.execute("SELECT * FROM fromSwitch")
#for row in cur.fetchall() :
#        for j in range(0, 3):
#                print row[j]

# Close all the cursors.
cur.close()

# Close all the databases.
db.close()



###########################################################################
# Note to self: eventually, the following can be incorporated:            #
# i) Remove the array-to-string section; it will be unneeded and the data #
#    can be interpreted directly from the array.			  #
#									  #
###########################################################################
