import logging 
#la configuration du logging pour enregister l'erreur dans un fichier
logging.basicConfig(
    filename='error.log',   
    level=logging.ERROR,   #le niveau d'erreur choisi dans cette cas    
)

def log_error(msg):
   logging.error(msg)


def read_file(filename):
    myfile=None
    try:
       myfile=open(filename,'r')
    except FileNotFoundError:
       log_error('ce fichier n\'existe pas')
    finally:
       #on doit vérifier si le fichier a ouvré d'abord:pour aviter le produit d'un erreur
       if myfile :
         myfile.close

read_file("notheeere")      
