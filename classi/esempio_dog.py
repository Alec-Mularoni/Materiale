class Dog:
    def __init__(self, nome, eta, peso):
        self.nome = nome
        self.eta = eta
        self.peso = peso
        
    def abbaia(self):
        print(f"{self.nome} sta abbaiando")
    
    def corre(self):
        print(f"{self.nome} sta correndo")

class Husky(Dog):
    def __init__(self, altezza):

        """  self.eta = eta
        self.peso = peso """
        self.altezza = altezza
    
    def dati(self):
        return self.nome, self.eta, self.peso, self.altezza

    def ulula(self):
        print(f"{self.nome} sta ululando")

cane1 = Dog("fiocco", 10, 5)
cane2 = Husky("Sky")

cane1.abbaia()
cane2.abbaia()
cane2.ulula()
        