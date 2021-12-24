#!/usr/bin/env python

import sys 
import socket
import time
​
rhost=sys.argv[1]
rport = 1337 #gives hint to start at port 1337
num = 0 #instructs us to begin at 0
​
while 1: #while True, meaning until the port equals 9765, do these actions. infinite loop
	try:
		s = socket.socket() # opens socket
		s.connect((rhost,rport)) # connects socket to victim IP and port 1337 as the room hints at
		if (port == 9765): # continue arithmetic until the final port 9765 is reached
			break
		newPort = newPort # stores new port each loop
		request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % rhost #bare minimum HTTP GET request, must end in \r\n\r\n, %s is string operator to read the rhost IP
		s.send(request.encode()) #encode the request
		response = s.recv(4096) #s.recv to receive the resulting data. The 4096 is a buffer for the data, so that you receive the data in manageable chunks
		httpResponse = repr(response) #the string containing the representation of the value s.recv() assigned to response, returns s.recv() inside the string resulting in "stringResponse"
		httpTrim = httpResponse[167:] #???????????????????????????????????????????????????????
		httpTrim = httpTrim.replace('\'','')
		data = list(httpTrim.split(" "))
		port = int(data[2]) #port must be integer
		print('Operation: '+data[0]+', number: '+ data[1]+', next port: '+ data[2]) #this is an array of what the port shows, operation, number, next port
		if(port != newPort): # ensures that each port randomly selected is not repeated
			if(data[0] == 'add'):
				num += float(data[1]) # keeps running total of sum in floating data form to use decimals
			elif(data[0] == 'minus'): 
				num -= float(data[1]) # running total of difference
			elif(data[0] == 'multiply'):
				num *= float(data[1])
			elif(data[0] == 'divide'):
				num /= float(data[1])
		s.close() # close the socket connection
	except: 	  # if the port equals 9765 then no longer try
		s.close()
		pass	  # a placeholder when a statement is required syntactically, but no code needs to be executed
​
print(num)
