class Tache:
    def __init__(self, id, titre, description, auteur, statut="TODO"):
        self.id = id
        self.titre = titre
        self.description = description
        self.statut = statut
        self.auteur = auteur

import json
import os

class GestionnaireTaches:
    def __init__(self, fichier="taches.json"):
        """
        Initialise le gestionnaire de tâches.
        - fichier : nom du fichier JSON pour sauvegarder/charger les tâches
        - taches : dictionnaire contenant toutes les tâches
        - compteur_id : pour attribuer un ID unique à chaque tâche
        - charge les tâches existantes depuis le fichier
        - crée le fichier s'il n'existe pas ou est vide
        """
        self.fichier = fichier
        self.taches = {}  
        self.compteur_id = 1
        self.charger_taches()  
        if not os.path.exists(self.fichier) or os.path.getsize(self.fichier) == 0:
            with open(self.fichier, "w", encoding="utf-8") as f:
                f.write("[]")  

    def charger_taches(self):
        """Charge toutes les tâches depuis le fichier JSON existant dans self.taches"""

    def sauvegarder_taches(self):
        """Sauvegarde toutes les tâches actuelles dans le fichier JSON"""

    def ajouter_tache(self, titre, description, auteur):
        """Ajoute une nouvelle tâche avec un ID unique et les informations fournies"""

    def supprimer_tache(self, id):
        """Supprime la tâche correspondant à l’ID fourni"""

    def lister_taches(self):
        """Retourne la liste de toutes les tâches présentes"""

    def changer_statut(self, id, nouveau_statut):
        """Modifie le statut d’une tâche donnée par son ID (TODO, DOING, DONE)"""

        