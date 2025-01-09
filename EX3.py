def read_file(filename):
    try:
       myfile=open(filename,'r')
    except FileNotFoundError:
       print("ce fichier n'existe pas")
    finally:
       #pour assurer que le fichier est fermé
       myfile.close
       
