# Prima parte del codice: uso del metodo open() e close()
"""
metodo tradizionale per scrivere e leggere file
"""

# Apertura del file 'prova2.txt' in modalità di scrittura ('w')
# Se il file non esiste, verrà creato; se esiste già, verrà sovrascritto
myfile = open("prova2.txt", "w")
myfile.write("\nciao 2")  # Scrive "ciao 2" con un a capo all'inizio
myfile.write("\nciao 2")  # Scrive "ciao 2" di nuovo, su una nuova riga
myfile.close()  # Chiude il file manualmente dopo la scrittura

# Apertura del file 'prova2.txt' in modalità di lettura ('r')
myfile = open("prova2.txt", "r")
# myfile.write("ciao")  # Questa riga è commentata perché la modalità 'r' non permette la scrittura
print(myfile.read())  # Legge e stampa il contenuto del file
myfile.close()  # Chiude manualmente il file dopo la lettura

# Seconda parte del codice: uso del costrutto 'with'
with open("prova.csv", "r+",) as myfile:
    print(myfile.read())  # Legge e stampa tutto il contenuto del file 'prova.csv'
    myfile.write("1,2,3,4,5")  # Aggiunge "1,2,3,4,5" alla fine del file


"""SPIEGAZIONE APERTURA FILE IN R+"""
#Lettura e scrittura su un file di testo 'prova.txt'
with open("prova.txt", "r+") as file:
    # Legge i primi 10 caratteri del file
    chunk = file.read(10)
    # print(chunk)  # Questa riga è commentata, ma avrebbe stampato i primi 10 caratteri letti

    # Posiziona il cursore a partire dal byte 13 del file
    file.seek(13)
    
    # Definisce una nuova stringa da scrivere a partire dalla posizione 13
    str_nuovo = "3\nriga 6"
    # Scrive la stringa "3\nriga 6" nel file a partire dal punto in cui il cursore è stato posizionato
    file.write(str_nuovo)
    
    # Scrive ulteriori tre righe vuote seguite da "riga 9"
    file.write("\n\n\nriga 9")
    
    # Legge il resto del file dopo le operazioni di scrittura e lo stampa
    chunk = file.read()
    print(chunk)

