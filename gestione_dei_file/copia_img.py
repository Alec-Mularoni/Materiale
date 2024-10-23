# Apertura del file originale 'husky.jpg' in modalità binaria di lettura ('rb')
# Il costrutto 'with' garantisce che il file venga chiuso automaticamente dopo l'uso
with open("husky.jpg", "rb") as img:
    
    # Legge tutte le righe del file binario e le memorizza in una lista
    row_to_list_img = img.readlines()

    # Apertura di un nuovo file 'copia.jpg' in modalità binaria di scrittura ('wb')
    # Questo creerà un nuovo file o sovrascriverà un file esistente con lo stesso nome
    with open("copia.jpg", "wb") as copia:
        
        # Inizializza un contatore per eventuali future elaborazioni (non utilizzato nel codice attuale)
        count = 0
        
        # Itera su ogni riga letta dal file originale e la scrive nel nuovo file
        for line in row_to_list_img:
            copia.write(line)  # Scrive la riga corrente nel file di copia
