# main.py
from server.serveur import ServeurTaches
from client.client import menu
import threading

# Lancer le serveur dans un thread daemon
thread_serveur = threading.Thread(target=lambda: ServeurTaches().demarrer(), daemon=True)
thread_serveur.start()
print("=== Serveur lancé sur 127.0.0.1:5000 ===")

# Lancer un client dans le même terminal
menu()
