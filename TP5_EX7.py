import shutil

with open("journal.txt",'w') as file:
   file.write('bounjour\n')
   file.write('Monsieur dans cette page')

try:
   shutil.copy("journal.txt","journal_copie.txt")
   print('file copied successfuly')
except FileNotFoundError:
   print('file to copy not found')
except IOError:
   print('problem while copying the file')

try:
   shutil.move("journal_copie.txt","archives")
   print('file moved successfuly')
except FileNotFoundError:
   print('file to move not found')
except IOError:
   print('problem while moving the file')
   
   