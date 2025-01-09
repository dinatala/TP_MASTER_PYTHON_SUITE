def get_positive_integer():
    
    integer=-1
    while integer<= 0:
      try:    
       integer=int(input("entrer un nombre positive:"))
       if integer <=0:
         print('le nombre doit etre positif')
      except ValueError:  
       print('valeur inseré unacceptable, entrer un nombre')


    print(f"valeur entrée:{integer}") 

get_positive_integer()    
    