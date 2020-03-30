#!/usr/bin/env python3

from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys
PORT = 5000
size = 8000
SERVER_IP   = '192.168.0.108'
PORT_NUMBER = 6000

hostName = gethostbyname( '' )
print(hostName)

mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket.bind( (hostName, PORT) )

print ("Server listening on ports " +  str(PORT) )

x=input("Press y if you want to listen and n to send\n")

if x=='y' or x=='Y':
    (data,addr) = mySocket.recvfrom(size)
    print("Sent by "+str(data))
    #print("Sent by "+ str(hostName) + " : " str(data))
    x=input("Press y if you want to listen and n to send")





else:
	print ("Sending packets to IP " +str(SERVER_IP) + " via port " + 	str(PORT_NUMBER))

	mySocket = socket( AF_INET, SOCK_DGRAM )


	x='y'


	while x=="y" or x=="Y":
		myMessage = input("Insert msg to send:\n")
		mySocket.sendto(myMessage.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
		x=input("Press y to continue or n to exit\n")
		if x=="n" or x=="N":
			sys.exit()
