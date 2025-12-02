# main.py
from server.serveur import ServeurTaches
import threading
import subprocess
import sys

def demarrer_serveur():
    serveur = ServeurTaches(host='127.0.0.1', port=5000)
    print("Serveur en cours de démarrage...")
    serveur.demarrer()

if __name__ == "__main__":
    # Lancer le serveur dans un thread daemon
    thread_serveur = threading.Thread(target=demarrer_serveur, daemon=True)
    thread_serveur.start()
    print("=== Serveur lancé sur 127.0.0.1:5000 ===\n")

    while True:
        choix = input("Voulez-vous lancer un client ? (o/n) : ").lower()
        if choix == 'o':
            # Lance un nouveau terminal Windows avec python client/client.py
            subprocess.Popen([
                "start", "cmd", "/k", f"python {sys.path[0]}\\client\\client.py"
            ], shell=True)
        elif choix == 'n':
            print("Fermeture du programme principal.")
            break
        else:
            print("Choix invalide, veuillez taper 'o' ou 'n'.")

