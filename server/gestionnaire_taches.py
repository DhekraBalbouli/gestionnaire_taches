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
        self.fichier = fichier
        self.taches = {}  
        self.compteur_id = 1
        self.charger_taches()  
        if not os.path.exists(self.fichier) or os.path.getsize(self.fichier) == 0:
            with open(self.fichier, "w", encoding="utf-8") as f:
                f.write("[]")  
    def charger_taches(self):
        """Charge les tâches depuis le fichier JSON s'il existe"""
        if os.path.exists(self.fichier):
            with open(self.fichier, "r", encoding="utf-8") as f:
                data = json.load(f)
                for t in data:
                    tache = Tache(
                        id=t["id"],
                        titre=t["titre"],
                        description=t["description"],
                        auteur=t["auteur"],
                        statut=t["statut"]
                    )
                    self.taches[tache.id] = tache
                if self.taches:
                    self.compteur_id = max(self.taches.keys()) + 1

    def sauvegarder_taches(self):
        """Sauvegarde les tâches dans le fichier JSON"""
        data = []
        for t in self.taches.values():
            data.append({
                "id": t.id,
                "titre": t.titre,
                "description": t.description,
                "auteur": t.auteur,
                "statut": t.statut
            })
        with open(self.fichier, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def ajouter_tache(self, titre, description, auteur):
        tache = Tache(self.compteur_id, titre, description, auteur)
        self.taches[self.compteur_id] = tache
        self.compteur_id += 1
        self.sauvegarder_taches()
        return tache

    def supprimer_tache(self, id):
        if id in self.taches:
            del self.taches[id]
            self.sauvegarder_taches()
            return True
        return False

    def lister_taches(self):
        return list(self.taches.values())

    def changer_statut(self,id, nouveau_statut):
        if id in self.taches:
            self.taches[id].statut = nouveau_statut
            self.sauvegarder_taches()
            return True
        return False