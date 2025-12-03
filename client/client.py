import socket
import json

class ClientTaches:
    def __init__(self, host='serveur_taches', port=5000):
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
        print("\n" + "="*40)
        print("           GESTION DES TÂCHES")
        print("="*40)
        print("1. Ajouter une tâche")
        print("2. Lister les tâches")
        print("3. Supprimer une tâche")
        print("4. Changer le statut")
        print("5. Quitter")
        choix = input("Votre choix : ").strip()

        if choix not in ["1","2","3","4","5"]:
            print("Choix invalide, veuillez réessayer.")
            continue

        if choix == "1":
            tache = {
                "action": "add",
                "titre": input("Titre : "),
                "description": input("Description : "),
                "auteur": input("Auteur : ")
            }
            print(client.envoyer_requete(tache))
        elif choix == "2":
            response = client.envoyer_requete({"action": "list"})
            try:
                taches = json.loads(response)
                print("\nListe des tâches :")
                print("-"*40)
                for t in taches:
                    print(f"ID: {t['id']} | [{t['statut']}] {t['titre']}")
                    print(f"Description: {t['description']}")
                    print(f"Auteur: {t['auteur']}")
                    print("-"*40)
            except json.JSONDecodeError:
                print("Erreur serveur ou réponse invalide :", response)

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
