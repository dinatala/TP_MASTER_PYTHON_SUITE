try:
    integer=-1 
    filename=None
    while integer<= 0 or filename==None:
       filename=input('entrer votre fichier:')  
       integer=int(input("entrer un nombre positive:"))
       if integer <=0:
         print('le nombre doit etre positif')
       with open ('filename','w') as fichier:
          fichier.write("bonjour a tous\n") 
       with open('filename','r')as fichier:
         contenu=fichier.read()
except ValueError:  
       print('valeur inseré unacceptable, entrer un nombre')
except FileNotFoundError:
      print('le fichier saisi n\'existe pas')
else:
   print(f"valeur entrée:{integer}") 
   print(f"le fichier est bien lu:{contenu}")


    
    
  
    



