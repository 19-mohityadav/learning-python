from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))

print("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)

    # decode bytes to string
    message = message.decode()

    # process (convert to uppercase)
    modifiedMessage = message.upper()

    # encode back to bytes before sending
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)