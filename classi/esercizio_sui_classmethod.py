class Prodotto:
    lista_prod = []

    def __init__(self, nome, prezzo, quantita):
        self.nome = nome
        self.prezzo = prezzo
        self.quantita = quantita

    @classmethod
    def aggiungi_prod(cls, nome, prezzo, quantita):
        # Crea un nuovo prodotto e lo aggiunge alla lista di classe
        nuovo_prodotto = cls(nome, prezzo, quantita)
        cls.lista_prod.append(nuovo_prodotto)
        return nuovo_prodotto # return mi posso salvarmi il mio prodotto
    
    @classmethod
    def mostra_prodotti(cls):
        # Mostra tutti i prodotti presenti nella lista
        for prodotto in cls.lista_prod:
            print(f"Nome: {prodotto.nome}, Prezzo: {prodotto.prezzo}, Quantità: {prodotto.quantita}")

# Creazione di un prodotto attraverso il metodo aggiungi_prod
Prodotto.aggiungi_prod('Scarpe', 59.99, 10)
Prodotto.aggiungi_prod('Maglietta', 19.99, 20)

#

# Visualizzazione dei prodotti
Prodotto.mostra_prodotti()























""" class Prodotto:
    # Attributo di classe per tenere traccia del numero totale di prodotti
    numero_prodotti = 0

    # Costruttore per inizializzare gli attributi del prodotto
    def __init__(self, nome, prezzo, quantita):
        self.nome = nome
        self.prezzo = prezzo
        self.quantita = quantita
        # Incrementa il numero totale di prodotti ogni volta che ne viene creato uno nuovo
        Prodotto.numero_prodotti += 1

    # Metodo di classe per mostrare il numero totale di prodotti creati
    @classmethod
    def mostra_numero_prodotti(cls):
        print(f"Numero totale di prodotti creati: {cls.numero_prodotti}")

    # Metodo per visualizzare le informazioni del prodotto
    def mostra_informazioni(self):
        print(f"Prodotto: {self.nome}, Prezzo: {self.prezzo}€, Quantità: {self.quantita}")
        

# --- Esempio d'uso ---

# Crea alcuni prodotti
prodotto1 = Prodotto("Mela", 0.5, 100)
prodotto2 = Prodotto("Arancia", 0.7, 150)
prodotto3 = Prodotto("Banana", 0.3, 200)

# Mostra le informazioni di ogni prodotto
prodotto1.mostra_informazioni()
prodotto2.mostra_informazioni()
prodotto3.mostra_informazioni()

# Usa il metodo di classe per mostrare il numero totale di prodotti creati
Prodotto.mostra_numero_prodotti() """
