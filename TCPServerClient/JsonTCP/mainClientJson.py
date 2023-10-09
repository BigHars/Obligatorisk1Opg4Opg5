from socket import *
import json

serverPort = 12012
serverName = 'localhost'

csock = socket(AF_INET, SOCK_STREAM)
csock.connect((serverName, serverPort))

method = input('What function would you ike to use? (random, add or subtract): ')
number1 = input('Your first number: ')
number2 = input('Your second number: ')

jsonData = {'method': method, 'number1': number1, 'number2': number2}
jsonString = json.dumps(jsonData)

csock.send(jsonString.encode())

dataBack = csock.recv(2048)
sentenceBack = dataBack.decode()

print('Recieved json data: ', sentenceBack)
csock.close()