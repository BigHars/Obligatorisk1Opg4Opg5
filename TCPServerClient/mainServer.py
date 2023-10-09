from socket import *
from threading import *
import random # importing the random module

serverPort = 12000

# method for one client
def handleClient(clientSocket, addr):
    sentence = clientSocket.recv(2048).decode()

    splittedText = sentence.split()
    Text = ''
    if(splittedText[0].lower() == 'add'):
        numberX = int(splittedText[1])
        numberY = int(splittedText[2])
        Text = f'{numberX} + {numberY} = {(numberX + numberY)}'
    elif(splittedText[0].lower() == 'subtract'):
        numberX = int(splittedText[1])
        numberY = int(splittedText[2])
        Text = f'{numberX} + {numberY} = {(numberX - numberY)}'
    elif(splittedText[0].lower() == 'random'):
        numberX = int(splittedText[1])
        numberY = int(splittedText[2])
        randomNumber = random.randint(numberX, numberY)
        Text = f'Random number between {numberX} and {numberY} is {randomNumber}'
    else:
        Text = f'The method {splittedText[0]} is not supported'


    clientSocket.send(Text.encode())
    clientSocket.close()

# Server setup
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready and running on port: ', serverPort)

while True:
    connectionSocket, addr = serverSocket.accept()
    print('Connected to client on: ', addr)
    Thread(target=handleClient, args=(connectionSocket, addr)).start()