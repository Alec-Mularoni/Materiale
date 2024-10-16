import math

class Punto:
    """
    Classe che rappresenta un punto in un piano cartesiano.

    Attributi:
    ----------
    x : float
        La coordinata x del punto.
    y : float
        La coordinata y del punto.
    """

    def __init__(self, x, y):
        """
        Inizializza un nuovo punto con le coordinate specificate.

        Parametri:
        ----------
        x : float
            La coordinata x del punto.
        y : float
            La coordinata y del punto.
        """
        self.x = x
        self.y = y
    
    def distanza(self, altro_punto):
        """
        Calcola la distanza euclidea tra questo punto e un altro punto.

        Parametri:
        ----------
        altro_punto : Punto
            Un altro oggetto di tipo Punto.

        Restituisce:
        ------------
        float
            La distanza tra questo punto e `altro_punto`.
        """
        return math.sqrt((altro_punto.x - self.x)**2 + (altro_punto.y - self.y)**2)
    
    def __str__(self):
        """
        Restituisce una rappresentazione in formato stringa del punto.

        Restituisce:
        ------------
        str
            Una stringa nel formato 'P(x, y)' che rappresenta il punto.
        """
        return f"P({self.x}, {self.y})"

# Creazione di istanze della classe Punto
p1 = Punto(1, 2)
p2 = Punto(3, 5)
p3 = Punto(10, 11)

# Calcolo della distanza tra i punti
p1.distanza(p2)
Punto.distanza(p1, p2)


class Percorso:
    """
    Classe che rappresenta un percorso costituito da una serie di punti.

    Attributi:
    ----------
    punti : list
        Una lista di oggetti di tipo Punto che costituiscono il percorso.
    """

    def __init__(self):
        """
        Inizializza un nuovo percorso vuoto.
        """
        self.punti = []

    def aggiungi(self, arg):
        """
        Aggiunge uno o più punti al percorso.

        Parametri:
        ----------
        arg : Punto o list di Punto
            Un singolo oggetto di tipo Punto oppure una lista di oggetti Punto.

        Eccezioni:
        -----------
        Exception
            Solleva un'eccezione se l'argomento passato non è né un Punto né una lista di Punti.
        """
        if isinstance(arg, Punto):
            self.punti.append(arg)
        elif isinstance(arg, list):
            self.punti.extend(arg)
        else:
            raise Exception("C'è un errore: l'argomento deve essere un Punto o una lista di Punti.")
    
    # Metodi obsoleti: ora gestiti da 'aggiungi'
    """
    # Metodi non più in uso, sostituiti dal metodo 'aggiungi'
    def aggiungi_punto(self, punto):
        self.punti.append(punto)
    
    def aggiungi_serie_di_punti(self, lista_punti):
        self.punti.extend(lista_punti)
    """

    def distanza_totale(self):
        """
        Calcola la distanza totale del percorso, somma delle distanze tra punti consecutivi.

        Restituisce:
        ------------
        float
            La distanza totale tra tutti i punti del percorso.
        """
        somma_distanze = 0
        for index in range(len(self.punti) - 1):
            punto = self.punti[index]
            altro_punto = self.punti[index + 1]
            somma_distanze += punto.distanza(altro_punto)
        return somma_distanze

    def mostra_punti(self):
        """
        Mostra tutti i punti presenti nel percorso.
        """
        for punto in self.punti:
            print(punto)


# Creazione di un percorso e aggiunta di punti
lista_punti = Percorso()
lista_punti.aggiungi([p1, p2, p3])  # Aggiunge una lista di punti
lista_punti.aggiungi(p1)  # Aggiunge un singolo punto
lista_punti.aggiungi(p2)
lista_punti.aggiungi(p3)

# Questa riga solleverà un'eccezione perché "stringa a caso" non è un oggetto Punto
# lista_punti.aggiungi("stringa a caso")  

# Mostra tutti i punti aggiunti al percorso
lista_punti.mostra_punti()

# Esempio di calcolo della distanza totale del percorso
print("Distanza totale del percorso:", lista_punti.distanza_totale())

"""
DESCRIZIONE


Obiettivo
L'obiettivo di questo esercizio è quello di implementare due classi in Python: Punto e Percorso. 
La classe Punto rappresenta un punto in un piano cartesiano, mentre la classe Percorso gestisce una serie di punti,
permettendo di calcolare la distanza totale tra di essi.

Descrizione delle Classi

Classe Punto:

La classe Punto deve avere un costruttore che accetta due argomenti: 
x e y, che rappresentano le coordinate del punto.
Implementa un metodo chiamato distanza, che prende un altro oggetto di tipo Punto come parametro e restituisce la distanza euclidea tra i due punti. 
Utilizza la formula: math.sqrt((x2-x1)**2+(y2-y1)**2) 
Implementa il metodo speciale __str__, che restituisce una stringa nel formato Punto(x, y)
per una rappresentazione facile del punto.

Classe Percorso:

La classe Percorso deve avere un costruttore che inizializza una lista vuota chiamata punti,
che servirà per memorizzare gli oggetti Punto.
Implementa un metodo chiamato aggiungi_punto, 
che accetta un oggetto Punto e lo aggiunge alla lista punti.
Implementa un metodo chiamato distanza_totale, 
che calcola e restituisce la distanza totale tra tutti i punti memorizzati nel percorso. 
La distanza totale è la somma delle distanze tra punti consecutivi.
Implementa un metodo chiamato mostra_punti, 
che stampa tutti i punti memorizzati nel percorso.
"""


