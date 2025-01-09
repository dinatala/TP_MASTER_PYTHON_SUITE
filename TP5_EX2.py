def user_data():
    data=[]
    for i in range(1,4):
       d=input(f"entrer la phrase {i}")
       data.append(d+"\n")
    with open ("phrases.txt","w")as fichier:
        fichier.writelines(data)
    with open ("phrases.txt","r") as fichier:
       lignes=fichier.readlines()
       for ligne in lignes:
        print(ligne)
    

user_data()
