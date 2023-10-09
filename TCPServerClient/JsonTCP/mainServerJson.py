from socket import *
import json
import threading
import random

serverPort = 12012

def handleClient(clientSocket, address):
    print('Conencted: ', address)

    sentence = clientSocket.recv(2048).decode()
    jsonData = json.loads(sentence)

    method = jsonData.get('method')

    response = {'method': method}

    if(method == 'random'):
        number1 = int(jsonData.get('number1', 0))
        number2 = int(jsonData.get('number2', 0))
        result = random.randint(number1, number2)
        response['number1'] = number1
        response['number2'] = number2
        response['result'] = result
    elif(method == 'add'):
        number1 = int(jsonData.get('number1', 0))
        number2 = int(jsonData.get('number2', 0))
        result = number1 + number2
        response['number1'] = number1
        response['number2'] = number2
        response['result'] = result
    elif(method == 'subtract'):
        number1 = int(jsonData.get('number1', 0))
        number2 = int(jsonData.get('number2', 0))
        result = number1 - number2
        response['number1'] = number1
        response['number2'] = number2
        response['result'] = result
    else:
        response = {'The method is not supported: ': method}

    responseJson = json.dumps(response)
    clientSocket.send(responseJson.encode())
    clientSocket.close()



serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
print("Server is ready and running...")

while True:
    clientSocket, address = serverSocket.accept()
    threading.Thread(target=handleClient, args=(clientSocket, address)).start()