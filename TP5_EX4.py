import csv 
donnes=[["nom","age","ville"],["sara",20,"Paris"],["Sakura",22,"Tokyo"]] 
       

with open("contacts.csv",mode="w",newline='')as fichier:
    ecrire=csv.writer(fichier)
    ecrire.writerows(donnes)
with open("contacts.csv",mode="r",newline='')as fichier:
    lire=csv.reader(fichier)
    for i in lire:
        print(i)
