class Dog():
    def __init__(self, nome, eta, peso, razza):
        self.nome = nome
        self.eta = eta
        self.peso = peso
        self.razza = razza
        
    def abbaia(self):
        print(f"{self.nome} sta abbaiando")
    
    def corre(self):
        print(f"{self.nome} sta correndo")


my_dog = Dog()