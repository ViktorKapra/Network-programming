# Network Programming Project


## Overview

This project is an example of simple client-sever communication. The client send to server name of historical figure. The server gets and information from two APIs and return respond to client.

## Architecture
 1.  `client.py` - send connects with surver via socket. Asks user for input. Send message to server and then recives the answer.
> #### Functions
> - `new_client()`- Sends requests to the server and then waits for an answer.
        
2.  `server.py` - connects to socket and listens. When it recieve connection request creates new thread that will continue the communication with client.
> #### Functions
>  * `new_connection(connection, address)` - perform communication with a certain client, generates responses.
> > -  receives parameters:
> >     -  `connection` new socket object usable to send and receive data on the connection
> >     -   `address` is the address bound to the socket on the other end of the connection.
>  * `get_info_about_author(message) ` - Collects full name and description about person from API(Wikipeida) and returned them.
> > -  receives parameters:
> >       - `message`- user input
>  * `get_quote_from_author(author_name) ` - Returns quote from given author. Makes request to API(Quotable.io) 
> > `author_name` - correct written name of author
<br>

## Examples

#### Example 1 
- Input :   
<pre><code> Please enter name of the person you want to ask about or 'quit' to exit:  Camus 
</code></pre>

- Output from server:
<pre><code> Albert Camus 
 French philosopher, journalist, and writer (1913–1960).
Famous quoute: Blessed are the hearts that can bend; they shall never be broken. 
</code></pre>

#### Example 2
- Input :   
<pre><code> Please enter name of the person you want to ask about or 'quit' to exit:  Maradona
</code></pre>

- Output from server:
<pre><code> Diego Maradona 
 Argentine football player and manager (1960–2020).
 No quotes  from Diego Maradona were found 
</code></pre>

