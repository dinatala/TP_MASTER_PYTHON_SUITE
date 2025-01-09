with open("example.txt","w") as fichier:
    fichier.write("le ligne 1 du fichier\n")
    fichier.write("le ligne 2 du fichier\n")
    fichier.write("le ligne 3 du fichier\n")
    fichier.write("le ligne 4 du fichier\n")
    fichier.write("le ligne 5 du fichier\n")
with open ("example.txt","r") as myfichier:
    lignes=myfichier.readlines()
    for ligne in lignes:
        print(ligne)
