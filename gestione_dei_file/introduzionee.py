# Usare il metodo 'open' senza 'with'
file = open('file_di_esempio.txt', 'r')  # Modalità di apertura in lettura ('r')
contenuto = file.read()  # Legge tutto il contenuto del file
print("Contenuto del file (open):")
print(contenuto)
file.close()  # Ricorda sempre di chiudere il file

# Usare 'with open' per gestire automaticamente la chiusura del file
with open('file_di_esempio.txt', 'r') as file:
    contenuto = file.read()
    print("\nContenuto del file (with open):")
    print(contenuto)

# Modalità di lettura del file:
# 1. read() --> Legge l'intero contenuto del file come stringa
with open('file_di_esempio.txt', 'r') as file:
    tutto_il_contenuto = file.read()
    print("\nContenuto letto con read():")
    print(tutto_il_contenuto)

# 2. readline() --> Legge una singola linea alla volta
with open('file_di_esempio.txt', 'r') as file:
    prima_linea = file.readline()
    print("\nContenuto letto con readline():")
    print(prima_linea)

# 3. readlines() --> Legge tutte le righe e le restituisce come una lista di stringhe
with open('file_di_esempio.txt', 'r') as file:
    tutte_le_linee = file.readlines()
    print("\nContenuto letto con readlines():")
    print(tutte_le_linee)

# 4. Iterare direttamente sul file per leggere riga per riga
with open('file_di_esempio.txt', 'r') as file:
    print("\nContenuto iterato riga per riga:")
    for linea in file:
        print(linea.strip())  # Rimuove newline extra

# Modalità di apertura del file in scrittura ('w')
file = open('file_di_esempio.txt', 'w')  # Modalità 'w' sovrascrive il file se esiste, crea un nuovo file se non esiste
file.write("Questo è un esempio di scrittura in modalità 'w'.\n")
file.write("Ogni scrittura in 'w' sovrascrive il file esistente.\n")
file.close()  # Ricorda sempre di chiudere il file

print("Contenuto del file (dopo apertura in modalità 'w'):")
with open('file_di_esempio.txt', 'r') as file:
    print(file.read())

# Usare 'with open' per la scrittura, che gestisce automaticamente la chiusura del file
with open('file_di_esempio.txt', 'w') as file:
    file.write("Scrivo un'altra riga in modalità 'w' con il blocco 'with'.\n")
    file.write("Questa operazione sovrascrive nuovamente il contenuto del file.\n")

print("\nContenuto del file (dopo apertura in modalità 'w' con 'with'):")
with open('file_di_esempio.txt', 'r') as file:
    print(file.read())

# Modalità di apertura in aggiunta ('a') - Aggiunge contenuto alla fine senza sovrascrivere
with open('file_di_esempio.txt', 'a') as file:
    file.write("Questa è una riga aggiunta con la modalità 'a'.\n")
    file.write("Non sovrascrive il contenuto esistente.\n")

print("\nContenuto del file (dopo apertura in modalità 'a'):")
with open('file_di_esempio.txt', 'r') as file:
    print(file.read())

# Modalità di apertura in lettura/scrittura ('r+')
with open('file_di_esempio.txt', 'r+') as file:
    file.write("Inizio del file modificato con 'r+'.\n")  # Sovrascrive l'inizio del file
    # Ora leggiamo il contenuto aggiornato
    file.seek(0)  # Torna all'inizio per leggere da capo
    print("\nContenuto del file (dopo apertura in modalità 'r+'): ")
    print(file.read())

# Modalità di apertura in scrittura esclusiva ('x') - Crea un file nuovo, fallisce se esiste
try:
    with open('nuovo_file.txt', 'x') as file:
        file.write("Questo file è stato creato con la modalità 'x'.\n")
    print("\nFile 'nuovo_file.txt' creato e scritto con modalità 'x'.")
except FileExistsError:
    print("\nIl file 'nuovo_file.txt' esiste già, quindi non può essere creato con modalità 'x'.")
