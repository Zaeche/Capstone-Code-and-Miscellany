#!/usr/bin/env python2.7

# Import from relevant header files and libraries
import serial, string, struct
import ctypes, os, mmap
import time, sys, datetime

# New empty map file:
file = os.open('/var/www/mmaptest', os.O_CREAT | os.O_TRUNC | os.O_RDWR)

# Calibrate to correct size:
assert os.write(file, '\x00' * mmap.PAGESIZE) == mmap.PAGESIZE

# Create an MMAP instance:
dataExchange = mmap.mmap(file, mmap.PAGESIZE, mmap.MAP_SHARED, mmap.PROT_WRITE)

# Create an integer and set it to a value:
i = ctypes.c_int.from_buffer(dataExchange)
i.value = 10
i.value += 1

assert i.value == 11

# Determine offsets and fix them:
offset = struct.calcsize(i._type_)
assert dataExchange[offset] == '\x00' 

# Create a string
s_type = ctypes.c_char * len('foo')
s = s_type.from_buffer(dataExchange, offset)
s.raw = 'foo'

print 'The first 10 bytes of the MMAP: %r' %dataExchange[:10]

