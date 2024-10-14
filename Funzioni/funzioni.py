# 1. Definizione di una funzione semplice con parametri e return
def somma(a, b):
    """Restituisce la somma di due numeri."""
    return a + b

risultato = somma(5, 3)
# risultato sarà 8


# 2. Funzione con parametri opzionali (default parameters)
def saluto(nome, messaggio="Ciao"):
    """Stampa un messaggio di saluto. 'messaggio' è opzionale."""
    return f"{messaggio}, {nome}!"

# Può essere chiamata con uno o due argomenti
saluto1 = saluto("Mario")
# saluto1 sarà "Ciao, Mario!"
saluto2 = saluto("Mario", "Buongiorno")
# saluto2 sarà "Buongiorno, Mario!"


# 3. Funzione con un numero variabile di argomenti (args)
def somma_tutti(*numeri):
    """Restituisce la somma di un numero arbitrario di argomenti."""
    return sum(numeri)

totale = somma_tutti(1, 2, 3, 4)
# totale sarà 10
var = 10
def delete(path, *args):
    var = None
    pass

delete("path", "-r")


# 4. Funzione con un numero variabile di argomenti chiave-valore (kwargs)
def descrizione_persona(**dati):
    """Restituisce una descrizione formattata di una persona."""
    descrizione = ", ".join([f"{chiave}: {valore}" for chiave, valore in dati.items()])

    return f"Descrizione: {descrizione}"

persona = descrizione_persona(nome="Mario", età=30, città="Roma")
# persona sarà "Descrizione: nome: Mario, età: 30, città: Roma"


# 5. Funzione annidata (nested function)
def esterna(messaggio):
    """Una funzione esterna che contiene una funzione interna."""
    def interna():
        """Funzione interna che accede alla variabile della funzione esterna."""
        return f"Messaggio dall'interna: {messaggio}"

    return interna()

messaggio = esterna("Ciao dal mondo!")
# messaggio sarà "Messaggio dall'interna: Ciao dal mondo!"


# 6. Funzione come oggetto (le funzioni possono essere assegnate a variabili)
def moltiplica(a, b):
    """Restituisce il prodotto di due numeri."""
    return a * b

operazione = moltiplica  # Assegniamo la funzione a una variabile
risultato = operazione(3, 4)
# risultato sarà 12


# 7. Funzione come parametro di un'altra funzione (funzioni di ordine superiore)
def applica_operazione(a, b, operazione):
    """Applica una funzione a due numeri."""
    return operazione(a, b)

risultato_somma = applica_operazione(5, 7, somma)
# risultato_somma sarà 12

risultato_moltiplicazione = applica_operazione(5, 7, moltiplica)
# risultato_moltiplicazione sarà 35


# 8. Funzione con valore di ritorno multiplo (tuple)
def coordinate():
    """Restituisce una coppia di coordinate."""
    x = 10
    y = 20
    return x, y  # Restituisce una tupla

x, y = coordinate()
# x sarà 10, y sarà 20


# 9. Funzione anonima (lambda)
doppio = lambda x: x * 2   # Funzione anonima che raddoppia il valore
risultato = doppio(5)
# risultato sarà 10

# Le lambda sono spesso usate con funzioni come map, filter e sorted
numeri = [1, 3, 5, 2, 4]
numeri_ordinati = sorted(numeri, key=lambda x: -x)
# numeri_ordinati sarà [5, 4, 3, 2, 1]


# 10. Funzione con decoratore
def maiuscolo_decoratore(func):
    """Un decoratore che trasforma il risultato di una funzione in maiuscolo."""
    def wrapper(*args, **kwargs):
        risultato = func(*args, **kwargs)
        return risultato.upper()
    return wrapper

@maiuscolo_decoratore
def saluta(nome):
    """Restituisce un messaggio di saluto."""
    return f"Ciao, {nome}"

saluto_maiuscolo = saluta("Mario")
# saluto_maiuscolo sarà "CIAO, MARIO"


# 11. Funzione ricorsiva (una funzione che si richiama da sola)
def fattoriale(n):
    """Restituisce il fattoriale di un numero n."""
    if n == 1:
        return 1
    else:
        return n * fattoriale(n - 1)

risultato_fattoriale = fattoriale(5)
# risultato_fattoriale sarà 120 (5! = 5 * 4 * 3 * 2 * 1)


# 12. Funzione con docstring (documentazione)
def esempio_documentato(a, b):
    """
    Restituisce la somma di a e b.

    Parametri:
    a -- il primo numero
    b -- il secondo numero

    Ritorna:
    La somma di a e b
    """
    return a + b

# Puoi accedere alla docstring con il comando help o __doc__
# esempio_documentato.__doc__ mostrerà la documentazione della funzione
lambda dati:[f"{chiave}: {valore}" for chiave, valore in dati.items()]