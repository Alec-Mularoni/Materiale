"""
DECORATORI IN PYTHON

Un decoratore è una funzione che consente di "avvolgere" un'altra funzione, aggiungendo del comportamento
extra prima o dopo l'esecuzione della funzione decorata, senza modificarne direttamente il codice.

I decoratori sono una funzionalità potente e flessibile di Python, spesso usata per il logging, 
il controllo degli accessi, la misurazione del tempo di esecuzione e altro ancora.

Struttura di base di un decoratore:
1. Il decoratore è una funzione che prende un'altra funzione come argomento.
2. All'interno del decoratore, c'è una funzione wrapper che contiene il codice aggiuntivo (comportamento extra).
3. Il decoratore restituisce la funzione wrapper, che sostituisce la funzione originale decorata.

In questo file, correggeremo il decoratore e spiegheremo i passi dettagliatamente.
"""

# Definiamo il nostro decoratore
def mio_decoratore(func):
    """
    Questo è un decoratore di esempio. Aggiunge del codice extra prima e dopo l'esecuzione
    della funzione che viene decorata.

    Args:
    - func (function): La funzione che verrà decorata.

    Returns:
    - wrapper (function): La funzione modificata che esegue il codice aggiuntivo e poi chiama la funzione originale.
    """
    def wrapper():
        # Codice eseguito prima della funzione decorata
        print("La funzione non è ancora eseguita")

        # Eseguiamo la funzione originale passata come argomento
        func()

        # Codice eseguito dopo la funzione decorata
        print("La funzione è stata eseguita")
        
        # Non restituiamo nulla perché la funzione decorata non restituisce nulla
        return None

    # Restituiamo la funzione wrapper, senza chiamarla immediatamente
    return wrapper

# Decoriamo la funzione `somma` con `@mio_decoratore`
@mio_decoratore
def somma():
    """
    Questa è una funzione che verrà decorata. Il suo scopo è semplicemente
    sommare due numeri e stampare il risultato.
    """
    print(10 + 12)

# Chiamiamo direttamente la funzione decorata
#somma()

"""
SPIEGAZIONE DEL CODICE:

1. `mio_decoratore(func)` è un decoratore che avvolge una funzione (in questo caso, `somma`).
   - Prima di chiamare la funzione `func()`, stampa "La funzione non è ancora eseguita".
   - Dopo aver chiamato `func()`, stampa "La funzione è stata eseguita".

2. La funzione `somma` è decorata con `@mio_decoratore`. Ciò significa che quando chiamiamo `somma()`,
   in realtà viene eseguita la funzione `wrapper()` all'interno di `mio_decoratore`, che include il comportamento
   aggiuntivo prima e dopo l'esecuzione della funzione originale.

3. La chiamata `somma()` eseguirà:
   - Prima: stampa "La funzione non è ancora eseguita".
   - Poi: esegue `somma()` (cioè stampa `22`).
   - Infine: stampa "La funzione è stata eseguita".

Correzioni fatte:
- Inizialmente, nel codice c'era un errore perché il decoratore veniva chiamato con `@mio_decoratore`
  ma all'interno della funzione `mio_decoratore`, la funzione `wrapper()` veniva eseguita immediatamente,
  cosa che impediva la decorazione corretta.
- Ora, la funzione `wrapper` viene restituita senza essere eseguita subito, permettendo al decoratore
  di agire correttamente quando la funzione decorata viene chiamata.
"""


"""
DECORATORI CON ARGOMENTI

Ora vedremo come gestire una funzione decorata che accetta degli argomenti. 
Il decoratore deve essere modificato per accettare qualsiasi numero di argomenti e passarli alla funzione originale.

- `*args`: raccoglie tutti gli argomenti posizionali.
- `**kwargs`: raccoglie tutti gli argomenti nominativi (keyword arguments).

Questa struttura permette al decoratore di funzionare con qualsiasi funzione, indipendentemente dal numero o tipo di argomenti.
"""

# Definiamo il decoratore che accetta funzioni con argomenti
def mio_decoratore(func):
    """
    Decoratore che aggiunge del comportamento extra prima e dopo l'esecuzione di una funzione.
    Può funzionare con funzioni che accettano qualsiasi numero di argomenti.
    """
    def wrapper(*args, **kwargs):
        print("La funzione non è ancora eseguita")

        # Eseguiamo la funzione originale con i suoi argomenti
        risultato = func(*args, **kwargs)

        # Codice eseguito dopo la funzione decorata
        print("La funzione è stata eseguita")
        return risultato

    # Restituiamo la funzione wrapper, senza chiamarla immediatamente
    return wrapper

# Decoriamo una funzione che accetta argomenti
@mio_decoratore
def somma(a, b):
    """
    Funzione che somma due numeri e stampa il risultato.
    
    Args:
    - a (int): Il primo numero.
    - b (int): Il secondo numero.
    
    Returns:
    - int: La somma dei due numeri.
    """
    print(f"La somma di {a} e {b} è {a + b}")
    return a + b  # Restituiamo il risultato della somma

# Chiamiamo la funzione decorata con argomenti
somma(10, 12)  # Eseguiamo la funzione somma con 10 e 12 come argomenti

"""
SPIEGAZIONE DEL CODICE:

1. `mio_decoratore(func)` è un decoratore che accetta una funzione con argomenti.
   - Il decoratore utilizza `*args` per gestire qualsiasi numero di argomenti posizionali.
   - Utilizza `**kwargs` per gestire qualsiasi numero di argomenti nominativi.

2. La funzione `somma(a, b)` prende due argomenti (a e b) e calcola la loro somma.
   - La funzione è decorata con `@mio_decoratore`, quindi il decoratore esegue codice aggiuntivo
     prima e dopo la funzione originale.

3. Quando chiamiamo `somma(10, 12)`, il decoratore:
   - Prima: stampa "La funzione non è ancora eseguita".
   - Poi: esegue la funzione `somma(10, 12)` che stampa "La somma di 10 e 12 è 22".
   - Infine: stampa "La funzione è stata eseguita".

Utilizzando `*args` e `**kwargs`, il decoratore può gestire funzioni con qualsiasi numero e tipo di argomenti,
rendendolo più flessibile.
"""

def decoratore(funzione):
    def wrapper():
        print(funzione())
        return funzione
    return wrapper

@decoratore
def somma():
    return 5+7


""" my_var = esterna("ciao")
print(esterna)
#print(esterna("ciao"))
print(my_var()) """



""" print(somma(1,2))
var = somma #
print(var(1,2)) """

