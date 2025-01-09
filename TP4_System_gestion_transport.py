# Classe Vehicule
class Vehicule:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee

    def afficher_info(self):
        print(f"Marque : {self.marque}")
        print(f"Modèle : {self.modele}")
        print(f"Année : {self.annee}")

# Classe Moteur
class Moteur:
    def __init__(self, puissance, type_moteur):
        self.puissance = puissance
        self.type_moteur = type_moteur

    def afficher_moteur(self):
        print(f"Puissance du moteur : {self.puissance}")
        print(f"Type de moteur : {self.type_moteur}")

# Classe Voiture :
class Voiture(Vehicule, Moteur):
    def __init__(self, marque, modele, annee, puissance, type_moteur, nombre_de_places):
        Vehicule.__init__(self, marque, modele, annee)
        Moteur.__init__(self, puissance, type_moteur)
        self.nombre_de_places = nombre_de_places

    def afficher_info(self):
        Vehicule.afficher_info(self)
        Moteur.afficher_moteur(self)
        print(f"Nombre de places : {self.nombre_de_places}")

# Classe Moto :
class Moto(Vehicule, Moteur):
    def __init__(self, marque, modele, annee, puissance, type_moteur, type_moto):
        Vehicule.__init__(self, marque, modele, annee)
        Moteur.__init__(self, puissance, type_moteur)
        self.type_moto = type_moto

    def afficher_info(self):
        Vehicule.afficher_info(self)
        Moteur.afficher_moteur(self)
        print(f"Type de moto : {self.type_moto}")



voiture = Voiture("Toyota", "Corolla", 2020, 132, "Essence", 5)
moto = Moto("Yamaha", "850j", 2022, 66, "Essence", "japane")

# Affichage des informations:
print("Informations de la Voiture :")
voiture.afficher_info()

print("\nInformations de la Moto :")
moto.afficher_info()
