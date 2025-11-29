import socket
import json

class ClientTaches:
    def __init__(self, host='127.0.0.1', port=5000):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))

    def envoyer_requete(self, requete):
        self.client_socket.sendall(json.dumps(requete).encode())
        response = self.client_socket.recv(4096).decode()
        return response


