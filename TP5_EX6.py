import os

try:
    os.rename("phrases.txt","anciennes_phrases.txt")
    print('fichier est renommé avec succées')
except FileNotFoundError:
    print('le fichier introuvable')
except IOError:
    print('probleme lors du renommage')

try:
    os.remove("anciennes_phrases.txt")
    print('fichier est supprimé avec succées')
except FileNotFoundError:
    print('le fichier à supprimé est introuvable')
except IOError:
    print('probleme lors du suppresion')
