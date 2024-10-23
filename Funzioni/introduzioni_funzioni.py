# funzioni_basilari.py

# Cos'è una funzione?
# Una funzione è un blocco di codice che puoi "riutilizzare" quando serve.
# Serve a evitare di riscrivere lo stesso codice più volte. 

# 1. Come definire una funzione
# Per creare una funzione, usiamo la parola chiave "def", seguita dal nome della funzione e delle parentesi.

def saluta():
    """Questa funzione stampa un saluto semplice."""
    print("Ciao, mondo!")
    pass

def prova():
    """ fare un doppio saluto"""
    pass

# 2. Come chiamare una funzione
# Una volta definita, puoi chiamare (usare) la funzione con il suo nome seguito da parentesi.

saluta()
# Questo chiamerà la funzione e stamperà "Ciao, mondo!"


# 3. Funzione con parametri
# Possiamo passare informazioni a una funzione usando i "parametri".
# Un parametro è come una variabile che vive solo all'interno della funzione.

def saluta_persona(nome):
    """Questa funzione saluta la persona che gli viene passata come parametro."""
    print(f"Ciao, {nome}!")

# Chiamiamo la funzione con un parametro
saluta_persona("Mario")
# Stampa "Ciao, Mario!"

saluta_persona("Luigi")
# Stampa "Ciao, Luigi!"


# 4. Funzione con ritorno di valori
# Le funzioni possono anche restituire (ritornare) un valore usando la parola chiave "return".
# Questo valore può essere usato in altre parti del programma.

def somma(a, b):
    """Questa funzione restituisce la somma di due numeri."""
    return a + b

# Possiamo salvare il risultato della funzione in una variabile
risultato = somma(5, 3)
print(risultato)
# Stampa 8


# 5. Parametri opzionali
# Possiamo dare un valore predefinito ai parametri. In questo modo, se l'utente non fornisce quel parametro, verrà usato il valore predefinito.

def saluto_personalizzato(nome, messaggio="Ciao"):
    """Questa funzione stampa un saluto personalizzato. Il messaggio è opzionale."""
    print(f"{messaggio}, {nome}!")

saluto_personalizzato("Mario")
# Stampa "Ciao, Mario!"

saluto_personalizzato("Luigi", "Buongiorno")
# Stampa "Buongiorno, Luigi!"


# 6. Funzioni con più parametri
# Una funzione può avere quanti parametri vogliamo.

def moltiplica(a, b, c):
    """Questa funzione restituisce il prodotto di tre numeri."""
    return a * b * c

risultato = moltiplica(2, 3, 4)
print(risultato)
# Stampa 24


# 7. Funzioni per riutilizzare codice
# Una delle cose migliori delle funzioni è che puoi riutilizzarle in qualsiasi momento,
# senza dover riscrivere il codice.

def quadrato(numero):
    """Questa funzione restituisce il quadrato di un numero."""
    return numero * numero

print(quadrato(5))  # Stampa 25
print(quadrato(10))  # Stampa 100


# 8. Docstring (Documentazione)
# Una docstring è una stringa che spiega cosa fa una funzione. Si scrive subito dopo il "def" e
# viene visualizzata quando usi la funzione help() o leggi la documentazione della funzione.
# È buona pratica aggiungere docstring a ogni funzione.

# Esempio di docstring:
def somma_due_numeri(a, b):
    """Questa funzione restituisce la somma di due numeri."""
    return a + b

# Puoi visualizzare la docstring usando la funzione help:
help(somma_due_numeri)
# Questo mostrerà: "Questa funzione restituisce la somma di due numeri."


