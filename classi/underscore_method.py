












'''class Punto:
    def __init__(self, x, y):
        """__init__ è usato per inizializzare un oggetto quando viene creato."""
        self.x = x
        self.y = y
    
    def __repr__(self):
        """__repr__ restituisce una rappresentazione ufficiale e non ambigua dell'oggetto."""
        return f'Punto({self.x}, {self.y})'
    
    def __str__(self):
        """__str__ restituisce una rappresentazione leggibile dell'oggetto (usata con print)."""
        return f'Punto con coordinate ({self.x}, {self.y})'
    
    def __add__(self, altro_punto):
        """__add__ è usato per sovraccaricare l'operatore + tra due oggetti Punto."""
        return Punto(self.x + altro_punto.x, self.y + altro_punto.y)
    
    def __eq__(self, altro_punto):
        """__eq__ è usato per confrontare due oggetti con l'operatore ==."""
        return self.x == altro_punto.x and self.y == altro_punto.y
        '''

'''
class Prodotto:
    def __init__(self, nome, prezzo):
        """Inizializza il prodotto con nome e prezzo."""
        self.nome = nome
        self.prezzo = prezzo

    def __repr__(self):
        """Rappresentazione ufficiale del prodotto."""
        return f"Prodotto('{self.nome}', {self.prezzo})"

    def __str__(self):
        """Rappresentazione leggibile del prodotto."""
        return f"{self.nome} - €{self.prezzo:.2f}"

    def __eq__(self, altro_prodotto):
        """Confronta due prodotti per nome e prezzo."""
        return self.nome == altro_prodotto.nome and self.prezzo == altro_prodotto.prezzo

    def __add__(self, altro_prodotto):
        """Sommare il prezzo di due prodotti."""
        return self.prezzo + altro_prodotto.prezzo


class Carrello:
    def __init__(self):
        """Inizializza un carrello vuoto."""
        self.prodotti = []

    def __len__(self):
        """Restituisce il numero di prodotti nel carrello."""
        return len(self.prodotti)

    def __getitem__(self, indice):
        """Permette di accedere ai prodotti tramite indicizzazione."""
        return self.prodotti[indice]

    def __setitem__(self, indice, prodotto):
        """Permette di aggiornare un prodotto tramite indice."""
        self.prodotti[indice] = prodotto

    def __delitem__(self, indice):
        """Permette di rimuovere un prodotto dal carrello tramite indice."""
        del self.prodotti[indice]

    def __str__(self):
        """Restituisce una rappresentazione leggibile del carrello e del totale."""
        if not self.prodotti:
            return "Il carrello è vuoto."
        
        elenco_prodotti = '\n'.join([str(prodotto) for prodotto in self.prodotti])
        totale = sum([prodotto.prezzo for prodotto in self.prodotti])
        return f"Carrello:\n{elenco_prodotti}\nTotale: €{totale:.2f}"

    def __call__(self, prodotto):
        """Aggiunge un prodotto al carrello con la sintassi di chiamata."""
        self.prodotti.append(prodotto)
        print(f"{prodotto.nome} aggiunto al carrello.")

    def __eq__(self, altro_carrello):
        """Confronta due carrelli per verificare se contengono gli stessi prodotti."""
        return self.prodotti == altro_carrello.prodotti


# Esempio di utilizzo
if __name__ == "__main__":
    # Creazione di alcuni prodotti
    mela = Prodotto("Mela", 0.50)
    banana = Prodotto("Banana", 0.75)
    arancia = Prodotto("Arancia", 0.80)

    # Creazione del carrello
    carrello = Carrello()

    # Aggiunta di prodotti al carrello utilizzando il metodo __call__
    carrello(mela)
    carrello(banana)

    # Visualizzazione del carrello
    print(carrello)

    # Accesso a un prodotto specifico tramite indicizzazione (__getitem__)
    print("\nProdotto al primo indice:", carrello[0])

    # Aggiornamento di un prodotto (__setitem__)
    carrello[1] = arancia
    print("\nDopo la modifica del secondo prodotto:")
    print(carrello)

    # Cancellazione di un prodotto (__delitem__)
    del carrello[0]
    print("\nDopo la rimozione del primo prodotto:")
    print(carrello)

    # Verifica del numero di prodotti nel carrello (__len__)
    print("\nNumero di prodotti nel carrello:", len(carrello))

    # Confronto di carrelli (__eq__)
    altro_carrello = Carrello()
    altro_carrello(arancia)
    print("\nCarrelli sono uguali?", carrello == altro_carrello)

    # Somma dei prezzi di due prodotti (__add__)
    somma_prezzi = mela + banana
    print(f"\nSomma del prezzo di mela e banana: €{somma_prezzi:.2f}")
'''