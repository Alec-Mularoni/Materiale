# gestione_spese.py
var1 = 1
def mostra_menu():
    """Mostra il menu con le opzioni per l'utente."""
    print("\n Menu Spese ".center(3, "-"),
          "\n1. Aggiungi una spesa",
          "\n2. Visualizza tutte le spese",
          "\n3. Cancella una spesa",
          "\n4. Esci",
          )


def aggiungi_spesa(spese):
    """Permette all'utente di aggiungere una nuova spesa."""
    descrizione = input("Inserisci la descrizione della spesa: ")
    importo = float(input("Inserisci l'importo della spesa: "))
    data = input("Inserisci la data della spesa (formato GG/MM/AAAA): ")
    
    spesa = {
        'descrizione': descrizione,
        'importo': importo,
        'data': data
    }
    
    spese.append(spesa)
    print(f"Spesa '{descrizione}' aggiunta con successo!")


def visualizza_spese(spese):
    """Visualizza tutte le spese inserite e calcola il totale."""
    if not spese:
        print("Non ci sono spese registrate.")
        return
    
    totale = 0
    print("\n--- Elenco delle spese ---")
    for spesa in spese:
        print(f"Descrizione: {spesa['descrizione']}, Importo: €{spesa['importo']:.2f}, Data: {spesa['data']}")
        totale += spesa['importo']
    
    print(f"\nTotale delle spese: €{totale}")


def cancella_spesa(spese):
    """Permette all'utente di cancellare una spesa specificando la descrizione."""
    descrizione = input("Inserisci la descrizione della spesa da cancellare: ")
    spese_cancellate = [spesa for spesa in spese if spesa['descrizione'] == descrizione]
    
    if spese_cancellate:
        for spesa in spese_cancellate:
            spese.remove(spesa)
        print(f"Spesa con descrizione '{descrizione}' cancellata con successo!")
    else:
        print(f"Nessuna spesa trovata con descrizione '{descrizione}'.")


def main():
    """Gestisce il menu interattivo per l'utente."""
    spese = []
    
    while True:
        mostra_menu()
        scelta = input("Scegli un'opzione (1-4): ")
        
        if scelta == '1':
            aggiungi_spesa(spese)
        elif scelta == '2':
            visualizza_spese(spese)
        elif scelta == '3':
            cancella_spesa(spese)
        elif scelta == '4':
            print("Uscita dal programma. Arrivederci!")
            break
        else:
            print("Opzione non valida. Riprova.")
print(__name__)

