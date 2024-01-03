# Network Programming Project


## Overview

This project is an example of simple client-sever communication. The client send to server name of historical figure. The server gets and information from two APIs and return respond to client.

## Architecture
> `client.py` - send connects with surver via socket. Asks user for input. Send message to server and then recives the answer.

>`server.py` - connects to socket and listens. When it recieve connection request creates new thread that will coninue the communication with client.
> # Functions
>   `new_connection(connection, address)` - perform communication with a certain client, generates responses.
> > *  receives parameters:
> >     -  `connection` new socket object usable to send and receive data on the connection
> >     -   `address` is the address bound to the socket on the other end of the connection.
> `def get_info_about_author(message) ` - Collects full name and description about person from API and returned them.
> > *  receives parameters:
> >       - `message`- user input
> `def get_info_about_author(message) ` - Collects information from API and trasfer it in suitable format




---
