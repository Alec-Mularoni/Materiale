"""
GESTIONE DEGLI ERRORI IN PYTHON

In Python, la gestione degli errori viene effettuata utilizzando le istruzioni `try`, `except`, `else`, `finally` e `raise`.
Queste istruzioni permettono di gestire le eccezioni in modo controllato, migliorando la robustezza e la leggibilità del codice.

1. TRY: Utilizzato per definire un blocco di codice nel quale si possono verificare errori.
2. EXCEPT: Utilizzato per gestire le eccezioni sollevate all'interno del blocco `try`.
3. ELSE: Eseguito se il blocco `try` non solleva alcuna eccezione.
4. FINALLY: Eseguito sempre, che si verifichi o meno un'eccezione.
5. RAISE: Utilizzato per sollevare un'eccezione in modo programmatico.

Di seguito, esamineremo ciascuno di questi costrutti con esempi pratici.

"""

def divisione(a, b):
    """
    Funzione per effettuare la divisione di due numeri.
    
    Args:
    - a (float): Il numeratore.
    - b (float): Il denominatore.
    
    Returns:
    - float: Il risultato della divisione.
    
    Solleva:
    - ValueError: Se il denominatore è zero.
    """
    if b == 0:
        raise ValueError("Il denominatore non può essere zero.")  # Solleva un'eccezione
    return a / b

def esempio_try_except():
    """
    Esempio di utilizzo di try ed except per gestire le eccezioni.
    """
    try:
        risultato = divisione(10, 0)  # Questa chiamata solleverà un'eccezione
        print(f"Risultato: {risultato}")
    except ValueError as e:  # Gestisce l'eccezione ValueError
        print(f"Errore: {e}")  # Stampa il messaggio di errore

def esempio_else():
    """
    Esempio di utilizzo di else in combinazione con try ed except.
    """
    try:
        risultato = divisione(10, 2)  # Nessuna eccezione qui
    except ValueError as e:
        print(f"Errore: {e}")
    else:
        # Questo blocco viene eseguito solo se non ci sono eccezioni
        print(f"Risultato della divisione: {risultato}")

def esempio_finally():
    """
    Esempio di utilizzo di finally.
    """
    try:
        risultato = divisione(10, 2)
        print(f"Risultato: {risultato}")
    except ValueError as e:
        print(f"Errore: {e}")
    finally:
        # Questo blocco viene eseguito sempre, che ci siano errori o meno
        print("Esecuzione del blocco finally.")

def esempio_raise():
    """
    Esempio di utilizzo di raise per sollevare un'eccezione.
    """
    try:
        divisione(10, 0)  # Solleverà un'eccezione
    except ValueError as e:
        print(f"Gestito l'errore: {e}")
        raise  # Rilancia l'eccezione per ulteriori gestioni

# Esecuzione degli esempi
if __name__ == "__main__":
    print("Esempio di try-except:")
    esempio_try_except()
    
    print("\nEsempio di try-except con else:")
    esempio_else()
    
    print("\nEsempio di try-except con finally:")
    esempio_finally()
    
    print("\nEsempio di raise:")
    try:
        esempio_raise()
    except ValueError as e:
        print("Eccezione finale gestita nel main.")

"""
SPIEGAZIONE DEL CODICE:

1. **try**: Il blocco di codice dove potrebbero verificarsi eccezioni. Se un'eccezione viene sollevata, il controllo passa al blocco `except`.

2. **except**: Cattura le eccezioni. Può specificare il tipo di eccezione da gestire (ad esempio, `ValueError`). Se l'eccezione sollevata corrisponde, il blocco `except` viene eseguito.

3. **else**: Questo blocco viene eseguito solo se il blocco `try` non solleva alcuna eccezione. È utile per eseguire codice che deve essere eseguito solo se il `try` ha avuto successo.

4. **finally**: Questo blocco viene eseguito sempre, indipendentemente dal fatto che si sia verificata un'eccezione o meno. È utile per il cleanup, come chiudere file o liberare risorse.

5. **raise**: Permette di sollevare eccezioni programmaticamente. Può essere utilizzato per rilanciare un'eccezione dopo averla gestita, permettendo ad altri livelli di gestirla ulteriormente.

Questi costrutti consentono una gestione robusta delle eccezioni, migliorando la stabilità e l'affidabilità del codice.
"""
