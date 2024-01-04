import socket
import threading
import time
import requests

REQUEST_WIKI = 'https://en.wikipedia.org/w/rest.php/v1/search/page?q='
REQUEST_QUOTABLE = 'https://api.quotable.io/quotes?limit=1&author='
IP = socket.gethostbyname(socket.gethostname())
PORT = 9999
ENCODING_DECODING_FORMAT = 'utf-8'
MESSAGE_SIZE_LIMIT = 4096
DISCONNECT = 'quit'


def new_connection(connection, address):
    print(f"{address} is connected.")

    while True:
        message = connection.recv(MESSAGE_SIZE_LIMIT).decode(ENCODING_DECODING_FORMAT)
        # print(f'{message} /') -- for checking the message that was received
        if message == DISCONNECT:
            break
        result = get_info_about_author(message)
        author_name = result[0]
        msg = result[1]
        print(author_name)
        #if author_name != " " :
        msg += get_quote_from_author(author_name)

        connection.send(msg.encode(ENCODING_DECODING_FORMAT))
        time.sleep(2)
        print("Server listens:")

    connection.close()

def get_info_about_author(message):
    try:
        request_message_str = REQUEST_WIKI + message + '&limit=1'
        #print(request_message_str)
        response = requests.get(request_message_str)
        result = response.json()

    except requests.exceptions.JSONDecodeError:
        result = {'title': " ", 'description': "Bad response from API.\n"}
    # print(result)  -- for checking the0 response that was receicved

    if len(result['pages']) == 0:
         msg = f" No information about {message} \n"
         author_name = "No information"
    else:
         msg = f"{result['pages'][0]['title']} \n {result['pages'][0]['description'].rstrip()}.\n"
         author_name = result['pages'][0]['title']
    return [ author_name, msg]

def get_quote_from_author(author_name):
    try:
        request_message_str = REQUEST_QUOTABLE  + author_name
        print(request_message_str)
        response = requests.get(request_message_str)
        result = response.json()

    except requests.exceptions.JSONDecodeError:
        result = {'title': " ", 'description': "Bad response from API.\n"}
    # print(result)   -- for checking the0 response that was receicved
    if result['count'] == 0:
         quote = f" No quotes  from {author_name} were found \n"
    else:
         quote = f"Famous quoute: {result['results'][0]['content']} \n"
    return quote


def start_server():
    print("Server started!")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen()
    print(f"Server is listening on {IP}:{PORT}")

    while True:
        connection, address = server.accept()
        print(f"{connection} \n {address}")
        thread = threading.Thread(target=new_connection, args=(connection, address))
        thread.start()
        print(f"Active connections: {threading.active_count() - 1}")


if __name__ == "__main__":
    start_server()
