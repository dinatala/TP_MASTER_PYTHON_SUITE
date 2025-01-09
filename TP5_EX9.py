f = open("journal.txt", "r")

text=f.read()
print(f"le nombre de caractere:{len(text)}\n")
print(f"le nombre de mots:{len(text.split())}\n")
print(f"le nombre de lignes:{text.count('\n')+1}")
f.close()