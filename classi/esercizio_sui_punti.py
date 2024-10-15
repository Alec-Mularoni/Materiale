import math

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
Utilizza la formula: radice((x2-x1)**2+(y2-y1)**2) 
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


