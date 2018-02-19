from socket import *

serverIP = '127.0.0.1'
serverPort = 2010
assignment = socket(AF_INET, SOCK_DGRAM)
 # declare an empty list that to hold the message(array of strings)
message = []

 # the list of operation users can perform
operation = input(
     """
            Math Server
            select an operation to perform:
            1: Addition
            2: Multiplication
            3: Modulus
            4: Division
            5: Subtraction
            

            _ _ _
            
            """

            )
# adding operation to message
message.append(str(operation))

# enter two values on which the operation will be performed
first_variable = input ('enter the 1st value: .....')
second_variable = input ('enter the 2nd value: ......')

# add the values to the message
message.append(str(first_variable))
message.append(str(first_variable))

# format message into [operation, first_variable, second_variable]
message = ','.join(message)

# send message to client-side
assignment.sendto(message, (serverIP, serverPort))


# receive result from server
server_result, server_address = assignment.recvfrom(4096)
print('server result: ' + server_result)

# close connection betwen client and server
assignment.close();





 
