def convert_to_int(value):
    try:
       convertion=int(value)
       return convertion
    except ValueError:
        print(' pas un valeur valide à converser ')


print(convert_to_int('abc'))