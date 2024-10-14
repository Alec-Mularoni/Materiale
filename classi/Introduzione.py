# COS'È UNA CLASSE?
# Una classe è come un modello o uno stampo che descrive come creare oggetti. 
# Un oggetto è un'istanza (un'esemplificazione) di una classe.
# Le classi in Python sono usate per rappresentare concetti reali o astratti, come nel nostro esempio, 
# dove la classe "Dipendenti" rappresenta una struttura per definire un dipendente di un'azienda.

# COS'È UN ATTRIBUTO DI ISTANZA?
# Un attributo di istanza è una variabile che appartiene a una specifica istanza (oggetto) di una classe.
# Viene creata all'interno del metodo __init__ e di solito dipende dai dati che passiamo quando creiamo un oggetto.
# Ogni istanza della classe ha i propri attributi che possono contenere valori diversi.

# COS'È UN METODO?
# Un metodo è una funzione definita all'interno di una classe. I metodi permettono agli oggetti di eseguire azioni.
# I metodi spesso lavorano sugli attributi di istanza dell'oggetto per realizzare delle funzionalità.

# COS'È UN ATTRIBUTO DI CLASSE?
# Un attributo di classe è una variabile definita all'interno della classe stessa (fuori dai metodi) e viene condivisa da tutte le istanze della classe.
# Mentre ogni istanza ha i propri attributi di istanza, gli attributi di classe sono comuni a tutti gli oggetti creati da quella classe.

class Dipendenti:  # Definizione della classe "Dipendenti"
    
    # VARIABILE DI CLASSE
    # Questa è un'attributo di classe. È condiviso tra tutte le istanze della classe.
    # In questo caso, tutte le istanze "Dipendenti" avranno un aumento di stipendio del 4% (1.04).
    dipendente_raise = 1.04

    def __init__(self, name: str, surname: str, age: int):
        """
        Metodo __init__: Questo è il costruttore della classe.
        Viene chiamato automaticamente quando creiamo una nuova istanza della classe "Dipendenti".
        Qui, vengono inizializzati gli attributi di istanza, cioè variabili che appartengono a ciascun oggetto Dipendente.
        
        Args:
        - name (str): Il nome del dipendente.
        - surname (str): Il cognome del dipendente.
        - age (int): L'età del dipendente.
        
        Attributi di istanza:
        - self.name: memorizza il nome del dipendente.
        - self.surname: memorizza il cognome del dipendente.
        - self.age: memorizza l'età del dipendente.
        - self.email: crea un'email basata sul cognome e nome del dipendente.
        """
        # Questi sono gli attributi di istanza. Ogni oggetto (dipendente) avrà il proprio "name", "surname", "age", e "email".
        self.name = name  # Attributo di istanza
        self.surname = surname  # Attributo di istanza
        self.age = age  # Attributo di istanza
        # Genera automaticamente l'email combinando il cognome e il nome.
        self.email = f"{surname}.{name}@company.com"  # Attributo di istanza
        # Prova: solo un attributo di istanza d'esempio.
        self.prova = "prova"  # Attributo di istanza

    @classmethod
    def stringa_mail(cls):
        """
        Metodo di classe: I metodi di classe possono accedere e modificare la variabile di classe, 
        ma non le variabili di istanza di specifici oggetti. Il primo parametro è 'cls' invece di 'self', 
        e rappresenta la classe stessa.
        
        Questo metodo restituisce una stringa generica ("mia mail"), ma in altri casi potrebbe essere utile 
        per manipolare o accedere agli attributi di classe.
        """
        return "mia mail"

    def __repr__(self):
        """
        Metodo speciale (dunder method): __repr__ viene chiamato quando vogliamo ottenere una rappresentazione "ufficiale" dell'oggetto.
        È utile per il debug e lo sviluppo. In questo esempio, restituisce semplicemente un messaggio di saluto con il nome del dipendente.
        """
        return f"Ciao {self.name}!"

# CREAZIONE DI OGGETTI (ISTANZE DELLA CLASSE)
# Qui stiamo creando due oggetti della classe Dipendenti.
# Quando chiamiamo Dipendenti("John", "Smith", 34), il metodo __init__ viene eseguito e crea un nuovo dipendente
# con nome "John", cognome "Smith", e età 34. Lo stesso avviene per "jacke" e "Will".
dip1 = Dipendenti("John", "Smith", 34)  # Prima istanza della classe
dip2 = Dipendenti("jacke", "Will", 55)  # Seconda istanza della classe

# Ogni istanza ha i propri attributi di istanza:
print(dip1.name)  # Stampa "John"
print(dip1.email)  # Stampa "Smith.John@company.com"
print(dip2.email)  # Stampa "Will.jacke@company.com"

# UTILIZZO DEI METODI DI CLASSE E DUNDER METHODS
# Eseguiamo il metodo stringa_mail() che è un metodo di classe e il metodo __repr__.
print(Dipendenti.stringa_mail())  # Stampa "mia mail"
print(repr(dip1))  # Stampa "Ciao John!"



""" p1 = Punto(1, 2)
p2 = Punto(3, 4)
nuovo_p = p1 + p2
Dipendeti.stringa_mail()
print(p1[0])
#print(dip1)
#print(dip2.saluta()) """

