# ChatSocketPython
Client-Server python application (simple chat)

## Instructions:
1. Run server.py in your machine(internet connection is required)
2. Run client.py in another terminal(it can be inside another machine but it has to be in the same local network)
3. *You can have multiple clients running but only one server in this case*

You can send messages to the server through the command line with the client
You can read the messages from each client in your server output

To disconnect your client typing **$quit**

To kill your server you have to kill close the terminal tab you are running your server


## How this application works?
- Client:
    The program will try to connect with the port on the IP and if the connection is successfull, it will be waiting for messages while the application is running. If you type $quit, the program will be disconnected(if you just kill the terminal the connection will be ended but the server will get a different message). If the program cannot connect with the server, it will show a error message("servidor indisponível") if you try to send a message.
    The message is codified to byte form and sent to the server. If the message pass, a success message will be received("Mensagem recebida com sucess!")
    
- Server:
    The server will bind the port and start listening for connections. If any connection is received, a thread is created to handle this client with the handle_client function, the messa received is decoded and interpreted. If the it's different from !DISCONNECT, it will be printed with the client Id and the time it was received on the server output. If it receives the !DISCONNECT message, the connection will be close and the thread which was running it will be killed.
