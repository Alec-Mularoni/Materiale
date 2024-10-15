# Formula: (x2-x1)**2+(y2-y1)**2



















""" import math
# Definisci la classe Punto
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Metodo per calcolare la distanza tra due punti
    def distanza(self, altro_punto):
        return math.sqrt((altro_punto.x - self.x)**2 + (altro_punto.y - self.y)**2)

    def __str__(self):
        return f"Punto({self.x}, {self.y})"

# Classe per gestire un percorso tra punti
class Percorso:
    def __init__(self):
        self.punti = []

    # Aggiungi un punto al percorso
    def aggiungi_punto(self, punto):
        self.punti.append(punto)

    # Calcola la distanza totale tra tutti i punti del percorso
    def distanza_totale(self):
        distanza_totale = 0
        for i in range(len(self.punti) - 1):
            distanza_totale += self.punti[i].distanza(self.punti[i+1])
        return distanza_totale

    def mostra_punti(self):
        for punto in self.punti:
            print(punto)

# --- Esempio d'uso ---

# Crea alcuni punti
punto1 = Punto(1, 1)
punto2 = Punto(2, 4)
punto3 = Punto(5, 6)

# Crea un percorso
percorso = Percorso()
percorso.aggiungi_punto(punto1)
percorso.aggiungi_punto(punto2)
percorso.aggiungi_punto(punto3)

# Mostra i punti e calcola la distanza totale
print("Punti nel percorso:")
percorso.mostra_punti()

print(f"\nDistanza totale: {percorso.distanza_totale():.2f} unità") """