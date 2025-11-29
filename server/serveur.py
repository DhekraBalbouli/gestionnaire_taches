import socket
import threading
import json
from gestionnaire_taches import GestionnaireTaches, Tache

class ServeurTaches:
    def __init__(self, host='127.0.0.1', port=5000):
        self.host = host
        self.port = port
        self.gestionnaire = GestionnaireTaches()

    def gerer_client(self, client_socket):
        while True:
            try:
                data = client_socket.recv(4096).decode()
                if not data:
                    break

                requete = json.loads(data)
                action = requete.get("action")

              
                if action == "add":
                    t = Tache(
                    id=int(requete.get("id", self.gestionnaire.compteur_id)),
                    titre=requete.get("titre", ""),
                    description=requete.get("description", ""),
                    auteur=requete.get("auteur", "")
                )
                    self.gestionnaire.ajouter_tache(t.titre, t.description, t.auteur)
                    client_socket.sendall(b"Tache ajoutee")


                elif action == "list":
                    taches = self.gestionnaire.lister_taches()
                    client_socket.sendall(json.dumps([{
                    "id": t.id,
                    "titre": t.titre,
                    "description": t.description,
                    "auteur": t.auteur,
                    "statut": t.statut
                } for t in taches], indent=4).encode())

                elif action == "del":
                    self.gestionnaire.supprimer_tache(requete["id"])
                    client_socket.sendall(b"Tache supprimee")

           
                elif action == "statut":
                    id_stat = int(requete.get("id"))  # conversion en entier
                    nouveau_statut = requete.get("nouveau_statut", "TODO").upper()
                    self.gestionnaire.changer_statut(id_stat, nouveau_statut)
                    client_socket.sendall(b"Statut modifie")

            except Exception as e:
                print("Erreur avec le client :", e)
                client_socket.sendall(f"Erreur serveur : {e}".encode())
                continue

        client_socket.close()

    def demarrer(self):
        serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serveur.bind((self.host, self.port))
        serveur.listen(5)

        print(f"Serveur lance sur {self.host}:{self.port}")

        while True:
            client_socket, _ = serveur.accept()
            print("Client connecte !")
            thread = threading.Thread(target=self.gerer_client, args=(client_socket,))
            thread.start()

if __name__ == "__main__":
    s = ServeurTaches()
    s.demarrer()
