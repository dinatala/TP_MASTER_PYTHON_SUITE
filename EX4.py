#créer l'exception personnalisé:
class NegativeAgeError(Exception):
   pass

def set_age(age):
     if age <0:
        raise NegativeAgeError ('age ne peux pas etre negatif')
     

#tester l'exception crée
try:
    set_age(-3)
    print('age est accept')
except NegativeAgeError as e:
    print(e)