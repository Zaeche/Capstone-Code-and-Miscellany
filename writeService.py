#!/usr/bin/env python2.7

# Import from relevant header files and libraries
import serial, string, struct
import ctypes, os, mmap, time
import time, sys, datetime
import MySQLdb


# Open file for reading:
file = os.open('/var/www/io_Data', os.O_RDONLY)

#Memory map the file:
dataExchange = mmap.mmap(file, mmap.PAGESIZE, mmap.MAP_SHARED, mmap.PROT_READ)

# The next step is to write the received data to the server. To this end, we do$
# Connect to the relevant database:
db = MySQLdb.connect(host="localhost", user="testUser", passwd="tester", db="testDatabase")

# Create a cursor object to execute queries

# Create an integer and set it to a value:
i = None
s = None

while 1:
	try:

		new_i, = struct.unpack('i', dataExchange[:4])
		new_s, = struct.unpack('2s', dataExchange[4:6])

		if i != new_i or s != new_s:
		
			# Insert received data into the table  
			# Go from an array to a string
			data_0 = ""
			data_1 = "ON"
			data_2 = "OFF" 
			data_3 = "test_2"
			data_4 = "test_3"
			
			switch_Name = "Light One"
			dataMessage = ""

			endval = len(new_s)
			for i in range(0, endval):
				data_0 += new_s[i]			
			#for i in range(2, endval):
			#        dataMessage += new_s[i]
			#for i in range (6, 10):
			#        data_2 += new_s[i]
			#for i in range (10, endval):
			#        data_3 += new_s[i]
			

			if new_s != None:
				try:
					if data_0 == 'ON':

						cur = db.cursor()
                                                cur.execute("""
							UPDATE testDatabase.statusTable
                                                        SET State=%s, Description=%s, Temperature=%s
                                                        WHERE Switch=%s
   	    	                                """,(data_1, data_3, data_4, switch_Name))

						#cur.execute("INSERT INTO statusTable(Switch, State, Description, Temperature) VALUES('%s','%s', '%s', '%s')" % (switch_Name, data_1, data_3, data_4))
						db.commit()
						cur.close()
		
					if data_0 == 'OF':
						
						cur = db.cursor()
						cur.execute("""
                                                        UPDATE testDatabase.statusTable 
                                                        SET State=%s, Description=%s, Temperature=%s 
                                                        WHERE Switch=%s
                                                """, (data_2, data_3, data_4, switch_Name))
						
						#cur.execute("INSERT INTO statusTable(Switch, State, Description, Temperature) VALUES('%s','%s', '%s', '%s')" % (switch_Name, data_2, data_3, data_4))
						db.commit()
						cur.close()

					if data_0 == 'fS':	
						#cur.execute("INSERT INTO statusTable(Switch, State, Description, Temperature) VALUES('%s','%s', '%s', '%s')" % (switch_Name, data_2, data_3, data_4))
						
						cur = db.cursor()			
						cur.execute("""
                                                        UPDATE fromSwitch
                                                        SET Switch=%s, Instruction=%s, Data=%s
                                                """, (data_3, data_4, switch_Name))
						cur.execute("INSERT INTO fromSwitch(Switch, Instruction, Data) VALUES('test_1', 'test_2', 'test_3')")

						db.commit()
						cur.close()
					
				except:
				        print 'Error! Try again later.'
				        db.rollback()

				# Close all the cursors.
				#cur.close()

				# Close all the databases.
				#db.close()

			# Update i and s to the new value sent by the system:
			i = new_i
			s = new_s

	except KeyboardInterrupt:
		print('Error! MMAP_Write not working!')
		break	
