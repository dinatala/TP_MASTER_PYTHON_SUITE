def process_input():
    try:
        user_input=int(input('enter un nombre:'))
        div=10/user_input
        

    except ValueError:
        print('value inacceptable pour convertir en int')
    except ZeroDivisionError:
        print('erreur de division par 0')
    #this bloc is executed if no error were raised
    else:
        print(f"le resultat:{div}")


process_input()