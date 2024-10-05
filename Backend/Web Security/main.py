import socket, threading

ENCODING = "utf8"

class Client(threading.Thread):
    def run(self):
        # initialize necessary variables
        spacing = ""
        clientHost = "127.0.0.1"
        clientPort = 12345
        clientAddress = (clientHost, clientPort)

        # open connection
        connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        print(spacing, "open")

        requestData = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog", "."]

        for datum in requestData:
            # send request to server
            print(spacing, "put:", datum)
            connection.sendto(datum.encode(ENCODING), clientAddress)

            # get response from server
            responseData, clientAddress = connection.recvfrom(1024)
            print(spacing, "get:", responseData.decode(ENCODING))

        # close connection
        connection.close()
        print(spacing, "close")

class Server(threading.Thread):
    def run(self):
        # initialize necessary variables
        count = 0
        spacing = "\t\t\t"
        serverHost = "127.0.0.1"
        serverPort = 12346
        serverAddress = (serverHost, serverPort)

        # open connection
        connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        connection.bind(serverAddress)

        print(spacing, "open")

        while 1:
            # get request from client
            requestData, clientAddress = connection.recvfrom(1024)
            print(spacing, "get:", requestData.decode(ENCODING))

            # process request
            count += 1

            if requestData.decode(ENCODING) == ".":
                responseData = "done"
            else:
                responseData = "ok [" + str(count) + "]"

            # send response to client
            print(spacing, "put:", responseData)
            connection.sendto(responseData.encode(ENCODING), clientAddress)

            # close connection
            if requestData.decode(ENCODING) == ".":
                break

        connection.close()
        print(spacing, "close")

class Attacker(threading.Thread):
    def run(self):
        # initialize necessary variables
        spacing = "            "
        clientHost = "127.0.0.1"
        clientPort = 12345
        clientAddress = (clientHost, clientPort)

        # open connection
        clientConnection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        clientConnection.bind(clientAddress)

        # initialize necessary variables
        serverHost = "127.0.0.1"
        serverPort = 12346
        serverAddress = (serverHost, serverPort)

        # open connection
        serverConnection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        print(spacing, "open")

        while 1:
            # get request from client
            clientRequestData, clientAddress = clientConnection.recvfrom(1024)
            print(spacing, "get:", clientRequestData.decode(ENCODING))

            # modify request (if desired)
            serverRequestData = clientRequestData.decode(ENCODING)

            if clientRequestData.decode(ENCODING) == "quick":
                serverRequestData = "big"
            if clientRequestData.decode(ENCODING) == "fox":
                serverRequestData = "bear"
            if clientRequestData.decode(ENCODING) == "jumps":
                serverRequestData = "runs"
            if clientRequestData.decode(ENCODING) == "lazy":
                serverRequestData = "hyper"
            if clientRequestData.decode(ENCODING) == "dog":
                serverRequestData = "rabbit"

            # send request to server
            print(spacing, "put:", serverRequestData)
            serverConnection.sendto(serverRequestData.encode(ENCODING), serverAddress)

            # get response from server
            serverResponseData, serverAddress = serverConnection.recvfrom(1024)
            print(spacing, "get:", serverResponseData.decode(ENCODING))

            # modify response (if desired)
            clientResponseData = serverResponseData.decode(ENCODING)

            # send response to client
            print(spacing, "put:", clientResponseData)
            clientConnection.sendto(clientResponseData.encode(ENCODING), clientAddress)

            if serverResponseData.decode(ENCODING) == "done":
                break

        # close connection
        serverConnection.close()
        clientConnection.close()
        print(spacing, "close")

print("  Client     Attacker     Server")
print("----------  ----------  ----------")

# create all threads
server = Server()
attacker = Attacker()
client = Client()

# start all threads
server.start()
attacker.start()
client.start()

# join all threads
server.join()
attacker.join()
client.join()