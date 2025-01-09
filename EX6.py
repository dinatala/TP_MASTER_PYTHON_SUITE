
def save_division(a,b):
  try:
    resultat= int(a/b)
    
  except ZeroDivisionError:
    print('erreur de division par zero')
  else:
    print(f"le returne du devison:{resultat}")
  finally:
    print('fin du programme')

save_division(4,2)

   
