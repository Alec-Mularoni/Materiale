class Dipendeti: #classe
    dipendente_raise = 1.04 # var di classe
    def __init__(self, name:str, surname:str, age:int):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = f"{surname}.{name}@company.com"
        self.prova = "prova"
    
    @classmethod
    def stringa_mail():
        return "mia mail"
    
    def __repr__(self):
        return f"Ciao {self.name}!"

dip1 = Dipendeti("John", "Smith", 34)
dip2 = Dipendeti("jacke", "Will", 55)

class Punto:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.lista_cord=[self.x, self.y]


""" p1 = Punto(1, 2)
p2 = Punto(3, 4)
nuovo_p = p1 + p2
Dipendeti.stringa_mail()
print(p1[0])
#print(dip1)
#print(dip2.saluta()) """

