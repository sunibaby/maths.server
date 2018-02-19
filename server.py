from socket import *

# create a TCP/IP socket
assignment = socket(AF_INET, SOCK_DGRAM)

# create server address

server_address = ('', 2010)
print('Server waiting for connection')

# Bind socket to the server_adderss
assignment.bind(server_address)

# Math function
def math(message):
    # split message to remove the comms ','
    message = message.split(',')

    # assign the values of the operation and variables

    operation = message[0]
    first_variable = int(message [1])
    second_variable = int(message[2])

    # perform operation
    if operation == '1':
        return first_variable + second_variable
    elif operation == '2':
        return first_variable * second_variable
    elif operation == '3':
        return first_variable % second_variable
    elif operation == '4':
        return first_variable / second_variable
    elif operation == '5':
        return first_variable - second_variable
    else:
       print('Please use a valid operation (add, multiply, modulus, division or subtraction)') 

   # wait for a connection using an infinite loop
while True:
    print('waiting for a connection....')
    # receive message from client and the client address
    client_message, client_address = assignment.recvfrom(4096)
    # compute the result
    result = str(math(client_message))
    #send result back to client
    assignment.sendto(result, client_address)
