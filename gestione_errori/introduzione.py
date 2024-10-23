"""
    Restituisce:
    ------------
    float
        Il risultato della divisione se non si verifica un errore.
    0
        Se viene sollevata un'eccezione di divisione per zero (ZeroDivisionError).

    Descrizione:
    ------------
    Questa funzione utilizza un blocco `try-except` per gestire eventuali errori di divisione
    per zero. Nel caso in cui il denominatore `b` sia zero, viene catturata l'eccezione `ZeroDivisionError`
    e viene visualizzato un messaggio appropriato. Il blocco `finally` assicura che la funzione
    restituisca sempre un valore, anche in caso di errore.
    
    La struttura `try-except` serve per gestire in modo sicuro situazioni che potrebbero causare
    errori durante l'esecuzione del codice. La parte `try` contiene il codice che si vuole eseguire
    e che potrebbe generare un errore. Se si verifica un errore specifico, l'eccezione viene catturata
    nel blocco `except`, dove può essere gestita senza che il programma si arresti.
    
    Infine, il blocco `finally` viene sempre eseguito, a prescindere dall'errore, per garantire
    la restituzione di un risultato anche in presenza di eccezioni.
"""
    

def div(a, b):
    ris = 0  # Inizializzazione del risultato a zero
    try:
        ris = a / b  # Tentativo di eseguire la divisione
        return ris  # Restituzione del risultato se la divisione ha successo
    except ZeroDivisionError as e:
        print("Non si divide per zero")  # Gestione dell'errore di divisione per zero
    finally:
        return ris  # Restituzione del risultato, sia che si verifichi un errore o meno


# Esempi di utilizzo della funzione div
print(div(4, 0))  # Caso di divisione per zero, dovrebbe restituire 0 e stampare il messaggio
print(div(4, 2))  # Divisione normale, dovrebbe restituire 2.0
