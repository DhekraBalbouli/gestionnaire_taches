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

def menu():
    client = ClientTaches()
    while True:
        print("\n1. Ajouter tâche\n2. Lister tâches\n3. Supprimer tâche\n4. Changer statut\n5. Quitter")
        choix = input("Choix : ")
        if choix == "1":
            tache = {
                "action": "add",
                "id": input("ID : "),
                "titre": input("Titre : "),
                "description": input("Description : "),
                "auteur": input("Auteur : ")
            }
            print(client.envoyer_requete(tache))
        elif choix == "2":
            print(client.envoyer_requete({"action": "list"}))
        elif choix == "3":
            id_del = int(input("ID à supprimer : "))
            print(client.envoyer_requete({"action": "del", "id": id_del}))
        elif choix == "4":
            id_stat = input("ID : ")
            nouveau = input("Nouveau statut (TODO/DOING/DONE) : ")
            print(client.envoyer_requete({"action": "statut", "id": id_stat, "nouveau_statut": nouveau}))
        elif choix == "5":
            break
        
if __name__ == "__main__":
    menu()
