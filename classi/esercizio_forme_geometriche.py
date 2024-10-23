'''import math

class Shape:
    """Classe base per le forme geometriche."""
    def area(self):
        raise NotImplementedError("Questo metodo deve essere implementato dalle sottoclassi.")

    def perimeter(self):
        raise NotImplementedError("Questo metodo deve essere implementato dalle sottoclassi.")

class Circle(Shape):
    """Classe per rappresentare un cerchio."""
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """Classe per rappresentare un rettangolo."""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    """Classe per rappresentare un triangolo."""
    
    def __init__(self, base, height):
        self.base = base
        self.height = height
        # Per semplicità, consideriamo un triangolo isoscele
        self.side_length = math.sqrt((self.base / 2) ** 2 + self.height ** 2)

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.base + 2 * self.side_length

# Funzione principale per testare le classi
def main():
    shapes = [
        Circle(5),           # Cerchio con raggio 5
        Rectangle(4, 6),     # Rettangolo con larghezza 4 e altezza 6
        Triangle(3, 4)       # Triangolo con base 3 e altezza 4
    ]

    for shape in shapes:
        print(f"L'area della forma {shape.__class__.__name__} è: {shape.area():.2f}")
        print(f"Il perimetro della forma {shape.__class__.__name__} è: {shape.perimeter():.2f}\n")

if __name__ == "__main__":
    main()

'''
        
    