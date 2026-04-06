from socket import *

serverName = "localhost"   # or use actual server IP
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input("Input lowercase sentence: ")

# convert string to bytes before sending
clientSocket.sendto(message.encode(), (serverName, serverPort))

# receive data (bytes)
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# decode bytes to string
print(modifiedMessage.decode())

clientSocket.close()