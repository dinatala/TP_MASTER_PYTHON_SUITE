try:
    with open("inexistant.txt",'r')as fichier:
        ligne=fichier.read()
        for i in ligne:
            print(i)
except FileNotFoundError:
    print("le fichier à lire n'existe pas")