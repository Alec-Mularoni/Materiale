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

class Dipendenti:  
    # VARIABILE DI CLASSE
    dipendente_raise = 1.04  # Aumento di stipendio del 4%
    numero_dipendenti = 0  # Contatore dei dipendenti

    def __init__(self, name: str, surname: str, age: int, stipendio: float, posizione: str = "Junior"):
        """
        Costruttore della classe Dipendenti.
        
        Args:
        - name (str): Nome del dipendente.
        - surname (str): Cognome del dipendente.
        - age (int): Età del dipendente.
        - stipendio (float): Lo stipendio del dipendente.
        - posizione (str, opzionale): Posizione lavorativa (default: "Junior").
        """
        self.name = name
        self.surname = surname
        self.age = age
        self.email = f"{surname}.{name}@company.com"
        self.stipendio = stipendio  # Nuovo attributo: stipendio del dipendente
        self.posizione = posizione  # Nuovo attributo: posizione lavorativa
        Dipendenti.numero_dipendenti += 1  # Incremento del numero totale dei dipendenti
    
    def calcola_aumento(self):
        """
        Applica l'aumento di stipendio secondo il valore della variabile di classe 'dipendente_raise'.
        """
        self.stipendio *= self.dipendente_raise

    def promuovi(self, nuova_posizione: str, aumento_percentuale: float):
        """
        Promuove il dipendente a una nuova posizione con un aumento di stipendio.
        
        Args:
        - nuova_posizione (str): La nuova posizione del dipendente.
        - aumento_percentuale (float): Percentuale di aumento dello stipendio.
        """
        self.posizione = nuova_posizione
        self.stipendio *= (1 + aumento_percentuale / 100)
    
    def __repr__(self):
        """
        Rappresentazione ufficiale dell'oggetto.
        """
        return f"Dipendente: {self.name} {self.surname}, Età: {self.age}, Posizione: {self.posizione}"

    def __str__(self):
        """
        Rappresentazione in formato stringa del dipendente.
        """
        return f"{self.name} {self.surname}, {self.posizione} - Stipendio: {self.stipendio}€, Email: {self.email}"

    @staticmethod
    def riepilogo_dipendenti(dipendenti):
        """
        Metodo statico per fornire un riepilogo dei dipendenti.
        
        Args:
        - dipendenti (list): Lista di oggetti Dipendenti.

        Returns:
        - str: Riepilogo dei dipendenti.
        """
        report = f"Numero totale di dipendenti: {len(dipendenti)}\n"
        report += "Dettagli dei dipendenti:\n"
        for dip in dipendenti:
            report += f"- {dip}\n"
        return report

    @classmethod
    def cambio_valore_raise(cls, nuovo_valore):
        """
        Modifica il valore dell'aumento di stipendio per tutti i dipendenti.
        """
        cls.dipendente_raise = nuovo_valore

    @classmethod
    def numero_totale_dipendenti(cls):
        """
        Restituisce il numero totale dei dipendenti creati.
        """
        return cls.numero_dipendenti

# Esempio di utilizzo della classe migliorata
if __name__ == "__main__":
    # Creazione di un elenco di dipendenti
    dipendenti = []

    # Creazione di due dipendenti
    dip1 = Dipendenti("Mario", "Rossi", 30, 30000)
    dip2 = Dipendenti("Luigi", "Verdi", 40, 35000, "Senior")

    # Aggiunta dei dipendenti alla lista
    dipendenti.append(dip1)
    dipendenti.append(dip2)

    # Stampa delle informazioni dei dipendenti
    print(dip1)
    print(dip2)

    # Calcolo dell'aumento per Mario
    dip1.calcola_aumento()
    print(f"Nuovo stipendio di {dip1.name}: {dip1.stipendio}€")

    # Promozione di Luigi
    dip2.promuovi("Manager", 10)
    print(f"Nuova posizione e stipendio di {dip2.name}: {dip2.posizione}, {dip2.stipendio}€")

    # Riepilogo dei dipendenti
    print(Dipendenti.riepilogo_dipendenti(dipendenti))


# CREAZIONE DI OGGETTI (ISTANZE DELLA CLASSE)
# Qui stiamo creando due oggetti della classe Dipendenti.
# Quando chiamiamo Dipendenti("John", "Smith", 34), il metodo __init__ viene eseguito e crea un nuovo dipendente
# con nome "John", cognome "Smith", e età 34. Lo stesso avviene per "jacke" e "Will".
dip1 = Dipendenti("John", "Smith", 34)  # Prima istanza della classe
dip2 = Dipendenti("jacke", "Will", 55)  # Seconda istanza della classe
dip1.print_nome()

dip1.dipendente_raise = 1.07
Dipendenti.dipendente_raise = 1.09 
dip1.cambio_valore_raise(1.08)
print(dip2.dipendente_raise)
""" dip1.cambio_valore_raise(1.07)
print(dip1.dipendente_raise)
Dipendenti.cambio_valore_raise(1.10)
print(dip1.dipendente_raise) """

# Ogni istanza ha i propri attributi di istanza:
print(dip1.dipendente_raise)
Dipendenti.cambio_valore_raise(1.06)

  # Stampa "John"
  # Stampa "Smith.John@company.com"
print(dip2.dipendente_raise)  # Stampa "Will.jacke@company.com"

# UTILIZZO DEI METODI DI CLASSE E DUNDER METHODS
# Eseguiamo il metodo stringa_mail() che è un metodo di classe e il metodo __repr__.
""" print(Dipendenti.stringa_mail())  # Stampa "mia mail"
print(repr(dip1))  # Stampa "Ciao John!" """



""" p1 = Punto(1, 2)
p2 = Punto(3, 4)
nuovo_p = p1 + p2
Dipendeti.stringa_mail()
print(p1[0])
#print(dip1)
#print(dip2.saluta()) """

