# Funzione per scrivere una lista di punti (coordinate) su un file di testo
def scrive_punti(arg: list):
    # Apre il file 'serie_punti.txt' in modalità scrittura ('w')
    # Se il file non esiste, viene creato; se esiste, il contenuto viene sovrascritto
    with open("serie_punti.txt", "w") as file_punti:
        # Cicla attraverso ogni coppia di valori (x, y) nella lista passata come argomento
        for item in arg:
            # Crea una stringa formattata separando i valori con una virgola e aggiunge un ritorno a capo
            stringa_attuale = f"{item[0]},{item[1]}\n"
            # Scrive la stringa nel file
            file_punti.write(stringa_attuale)

# Chiamata della funzione con una lista di tuple e liste contenenti coppie di numeri
scrive_punti([(1, 2), [3, 4], (5, 6)])

# Funzione per sostituire una specifica riga nel file 'serie_punti.txt'
def replace_punti(riga: int, x: int, y: int):
    # Apre il file 'serie_punti.txt' in modalità lettura e scrittura ('r+')
    with open("serie_punti.txt", "r+") as f:
        # Legge tutte le righe del file e le memorizza in una lista
        lista_di_righe = f.readlines()
        # Sostituisce la riga specificata (indice riga - 1, poiché le liste partono da 0) con nuovi valori x e y
        lista_di_righe[riga - 1] = f"{x},{y}\n"
        # Riporta il cursore all'inizio del file
        f.seek(0)
        # Sovrascrive il file con la lista aggiornata delle righe
        f.writelines(lista_di_righe)


# Esempio di chiamata della funzione replace_punti per modificare la seconda riga
replace_punti(2, 2, 4)




