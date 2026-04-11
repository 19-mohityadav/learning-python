from socket import *

serverPort = 12000 # OPEN : http://localhost:12000/
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)

print("Server running on port", serverPort)

while True:
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(2048).decode()
        filename = message.split()[1].lstrip("/")

        if filename == "":
            filename = "index.html"

        f = open(filename, "rb")
        outputdata = f.read()
        f.close()

        # Detect content type
        if filename.endswith(".html"):
            content_type = "text/html"
        elif filename.endswith(".css"):
            content_type = "text/css"
        else:
            content_type = "text/plain"

        connectionSocket.send(f"HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send(f"Content-Type: {content_type}\r\n\r\n".encode())
        connectionSocket.sendall(outputdata)

    except:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<h1>404 Not Found</h1>".encode())

    connectionSocket.close()