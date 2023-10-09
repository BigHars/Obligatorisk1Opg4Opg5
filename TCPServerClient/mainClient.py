from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

function = input('What function would you ike to use? (random, add or subtract): ')
number1 = int(input('Your first number: '))
number2 = int(input('Your second number: '))

command = f'{function} {number1} {number2}'

clientSocket.send(command.encode())

response = clientSocket.recv(2048).decode()
print('Answer from server: ', response)

clientSocket.close()