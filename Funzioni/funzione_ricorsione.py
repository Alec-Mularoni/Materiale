def fattoriale(n):
    # Caso base: il fattoriale di 0 o 1 è 1
    if n == 0 or n == 1:
        return 1
    # Caso ricorsivo: n! = n * (n-1)!
    return n * fattoriale(n - 1)
        
# Esempio di utilizzo
numero = 5
print(f"Il fattoriale di {numero} è {fattoriale(numero)}")
