# Esempio con r+
try:
    with open('esempio_r+.txt', 'r+') as file:
        contenuto = file.read()  # Legge il contenuto esistente
        print("Contenuto prima con r+:\n", contenuto, end="")
        file.seek(0)  # Torna all'inizio
        file.write("Modifica con r+\n")  # Sovrascrive l'inizio del file
        file.seek(0)  # Torna all'inizio
        print("Contenuto dopo con r+:", file.read())  # Legge il contenuto modificato
except FileNotFoundError:
    print("Il file non esiste, r+ richiede un file esistente.")

# Esempio con w+
with open('esempio_w+.txt', 'w+') as file:
    file.write("Contenuto scritto con w+\n")  # Scrive, cancellando tutto il contenuto esistente
    file.seek(0)  # Torna all'inizio
    print("Contenuto dopo con w+:", file.read())  # Legge il nuovo contenuto
