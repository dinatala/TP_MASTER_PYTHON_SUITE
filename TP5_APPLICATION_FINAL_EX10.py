import csv 

donnes = [['sara',123]]

def ajouter_contacts():
  nom=input('ajouter un nom ')
  numero=input('ajouter un numero')
  donnes.append([nom.lower(),numero])
  with open("contacts.csv",mode="w",newline='')as fichier:
    ecrire=csv.writer(fichier)
    ecrire.writerows(donnes)
def afficher_contacts():
   with open("contacts.csv",mode="r",newline='')as fichier:
    lire=csv.reader(fichier)
    for i in lire:
        print(i)
def chercher_contact():
   nom=input("entrer nom du contact cherche : ").lower()
   for i in  range(0,len(donnes)):
      if donnes[i][0]==nom:
        print(f"votre contact trouvé:{donnes[i][1]}")
        break
      else:
         print('nom introuvable')
def supprimer_contact():
   nom=input("entrer nom du contact à supprimer : ").lower()
   for i in  range(0,len(donnes)):
      if donnes[i][0]==nom:
        del(donnes[i])
        print(f"votre contact est supprimé avec succées")
        break
      else:
         print('nom introuvable')
     
      
ajouter_contacts()
afficher_contacts()
chercher_contact()
supprimer_contact()
