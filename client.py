#!/usr/bin/python # This is client.py file
import socket # Import socket module
s = socket.socket() # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345 # Reserve a port for your service.
s.connect((host, port))
a= str(input("Enter First Number: "))
b= str(input("Enter Second Number: "))

summation = a+','+b

s.send(summation.encode('utf-8'))
f=s.recv(1024)
f=f.decode()
print (f)

s.close # Close the socket when done
