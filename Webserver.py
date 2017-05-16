'''
#Developers: Minh Phung and Christopher Blake Matis
#Course: CSC 138
#Socket Programming Assignment 2: Web Server

#Project Objective/Functions
Receives request, parse files and sends file
via tcp connection including an http response
or an error if the file is not found.
'''

from socket import *
serverPort = 8000

#Sock_STREAM for tcp socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)

#Message the client will receive from the server.
sentMessage = ''

print ('The Web server is up on port: ', serverPort)

while True:
    print ("Ready to receive HTTP request via web browser (Chrome or Firefox)")
    print("Accessible files that can be requested include (localhost:'portnumber'/hello.html)")
    print("as well as (localhost:'portnumber'/ReadMe.html)")
    connectionSocket, addr = serverSocket.accept()
    try:
        request = connectionSocket.recv(1024)
        #This will print the original form of request
        print ("Origin form of request: ->> ", request)
        #request is in bytes form b'GET /fileName etc..
        #using split() to get the fileName from request
        fileName = request.split()[1]
        #open file name, if file not exit throw in error
        fileHandle = open(fileName[1:])
        #if file exit, read from file
        retrieveData = fileHandle.read()
        #this will print the contents of the file
        print (retrieveData)
        #http header
        http_response = "\nHTTP/1.1 200 OK\n\n"
        #send http response
        sentMessage = http_response.encode()
        connectionSocket.sendall(sentMessage)
        #send file content to browser
        sentMessage = retrieveData.encode()
        connectionSocket.sendall(sentMessage)
        #close file
        fileHandle.close()
        #close TCP connection
        connectionSocket.close()
    except IOError:
        pass
        #http header
        http_response2 = "\nHTTP/1.1 404 Not Found\n\n"
        #file not found exit
        print ('404 Not Found')
        #send HTTP response
        connectionSocket.send(http_response2.encode())
        
        #send the 404 not found error to the client as well
        connectionSocket.send('404 Not Found')
        #close connection
        connectionSocket.close()
    print ("Webserver closed after one request")
    break
#this web server is intended to process only 1 request

