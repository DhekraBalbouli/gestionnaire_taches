gestionnaire_taches

Application Python client-serveur pour gérer des tâches : ajouter, lister, supprimer et changer le statut.

Le projet implémente une architecture client–serveur, où le serveur gère la logique et stocke les données, et le client envoie des requêtes via des sockets TCP.

📌 Fonctionnalités Implémentées
✔ Côté Serveur

Démarrage d’un serveur TCP sur un port donné

Réception et traitement des requêtes JSON

Gestion des tâches :

Ajouter une tâche

Lister les tâches

Supprimer une tâche

Modifier le statut (TODO → DOING → DONE)

Réponses encodées en JSON

Gestion d’une liste de tâches en mémoire

✔ Côté Client

Connexion au serveur TCP

Menu interactif dans le terminal

Envoi de requêtes JSON au serveur

Affichage des résultats reçus

Gestion des erreurs (choix invalide, réponse incorrecte, etc.)

🚀 Lancer le projet sans Docker
1️⃣ Prérequis

Python 3 installé

Avoir les fichiers :

serveur.py

gestionnaire_taches.py

client.py

2️⃣ Lancer le serveur (local)

Dans un terminal :

python serveur.py


Le serveur démarre généralement sur :

Serveur lancé sur 127.0.0.1:5000

3️⃣ Lancer un client (terminal local)

Dans un autre terminal :

python client.py


Tu peux lancer plusieurs clients en ouvrant plusieurs terminaux.

🐳 Lancer le projet avec Docker (serveur uniquement)
1️⃣ Construire l’image du serveur

Depuis le dossier docker/ :

docker build -t gestionnaire_taches_server -f Dockerfile_server .

2️⃣ Lancer le serveur dans un conteneur
docker run -it -p 5000:5000 --name serveur_taches gestionnaire_taches_server


Le serveur écoute sur le port 5000 et est accessible depuis le client local : 127.0.0.1:5000.

⚠ Pour l’instant, seul le serveur est dockerisé. Le client doit être lancé localement depuis ton PC.

📁 Structure du Projet
mini_projet_gestionnaire_tache/
│
├── server/
│   ├── serveur.py
│   ├── gestionnaire_taches.py
│
├── client/
│   ├── client.py
│
├── docker/
│   ├── Dockerfile_server
│   └── Dockerfile_client (à créer si besoin)
│
└── README.md

🛠 Technologies Utilisées

Python (socket, threading, JSON)

Docker

Communication TCP/IP

👩‍💻 Auteure

Projet réalisé par Dhekra Balbouli, Licence Technologie de l’Information – ISET Bizerte.