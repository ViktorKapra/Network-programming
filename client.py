import socket
import sys

IP = socket.gethostbyname(socket.gethostname())
PORT = 9999
ENCODING_DECODING_FORMAT = 'utf-8'
MESSAGE_SIZE_LIMIT = 4096
DISCONNECT = 'quit'


def new_client():
    while True:
        person_name = input("Please enter name of the person you want to ask about or 'quit' to exit: ")
        if person_name.isnumeric():
            print("Input is not valid. Connection is closed!")
            sys.exit(0)
        client.send(person_name.encode(ENCODING_DECODING_FORMAT))
        if person_name == DISCONNECT:
            sys.exit(0)

        server_message = client.recv(MESSAGE_SIZE_LIMIT).decode(ENCODING_DECODING_FORMAT)
        print(f"{server_message}")


if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((IP, PORT))
    print(f"Client connected to server at {IP}:{PORT}")
    new_client()
