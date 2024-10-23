# Introduzione alle variabili in Python

# In Python, le variabili sono utilizzate per memorizzare dati. Non è necessario dichiarare il tipo della variabile, Python lo deduce automaticamente.

# Esempi di variabili:
a = 10            # Variabile intera
b = 3.14          # Variabile di tipo float (numero decimale)
c = "Hello"       # Variabile di tipo stringa
d = [1, 2, 3, 4]  # Variabile di tipo lista (mutabile)
e = (5, 6, 7)     # Variabile di tipo tupla (immutabile)
f = {"chiave": "valore"}  # Variabile di tipo dizionario (mutabile)

# Stampa delle variabili per verificarne il contenuto
print("Valore di a:", a)
print("Valore di b:", b)
print("Valore di c:", c)
print("Valore di d:", d)
print("Valore di e:", e)
print("Valore di f:", f)

# Tipi immutabili
# In Python, alcuni tipi di dati sono "immutabili", il che significa che il loro valore non può essere modificato una volta assegnato.
# Esempi di tipi immutabili: int, float, string, tuple

# Modificare un intero o una stringa crea un nuovo oggetto
a = 20   # 'a' ora punta a un nuovo oggetto intero con valore 20
c = "Ciao"  # 'c' ora punta a una nuova stringa "Ciao"
# Nota: il valore precedente non è modificato, ma sostituito

# Tipi mutabili
# Alcuni tipi di dati sono "mutabili", il che significa che possono essere modificati senza cambiare la loro identità.
# Esempi di tipi mutabili: list, dict, set

# Esempio con una lista (mutabile)
d.append(5)  # Aggiunge l'elemento 5 alla lista 'd'
print("Lista modificata d:", d)

# Esempio con un dizionario (mutabile)
f["nuova_chiave"] = "nuovo_valore"  # Aggiunge una nuova coppia chiave-valore al dizionario
print("Dizionario modificato f:", f)

# Differenza chiave tra mutabili e immutabili:
# Quando modifichi un oggetto mutabile, stai effettivamente modificando l'oggetto stesso.
# Quando modifichi un oggetto immutabile, crei un nuovo oggetto e assegni la variabile a quell'oggetto.

# Esempio di comportamento di un oggetto mutabile e immutabile:

# Oggetto immutabile (tupla)
tupla1 = (1, 2, 3)
# tupla1[0] = 100  # Questo causerebbe un errore perché le tuple non possono essere modificate

# Oggetto mutabile (lista)
lista1 = [1, 2, 3]
lista1[0] = 100  # Questo è consentito perché le liste sono mutabili
print("Lista modificata lista1:", lista1)

# Funzione per mostrare l'identità degli oggetti
def mostra_identita(var):
    print(f"L'identità dell'oggetto {var} è:", id(var))

# Mostra identità per tipi mutabili e immutabili
mostra_identita(tupla1)  # Identità immutabile
mostra_identita(lista1)  # Identità mutabile (rimane la stessa anche dopo modifiche)
