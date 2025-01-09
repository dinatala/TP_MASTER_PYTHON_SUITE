def user_data():
        
    with open ("phrases.txt","a")as fichier:
        data=[]
        stop="non"
        reponse=input("tu veux ajouter d'autres phrases au fichier? repondre avec :oui/non").lower()
        if reponse=="oui":
            while stop=="non":    
             s=input(f"entrer votre  phrase ")
             data.append(s+"\n")
             stop=input("tu veux arreter?oui/non").lower()

        fichier.writelines(data)
    with open ("phrases.txt","r") as fichier:
       lignes=fichier.readlines()
       for ligne in lignes:
        print(ligne)
    
user_data()
