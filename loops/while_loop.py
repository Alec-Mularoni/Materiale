"""
WHILE LOOP IN PYTHON

Un ciclo `while` in Python esegue un blocco di codice finché una condizione rimane vera.
È utile quando non si sa esattamente quante volte un'operazione debba essere ripetuta, ma si sa
che deve continuare fino a quando una condizione è soddisfatta.

Sintassi di base:

while condizione:
    # blocco di codice da eseguire finché la condizione è vera

- `condizione`: è un'espressione che viene valutata come True o False.
- Il ciclo continua finché `condizione` è vera. Quando diventa falsa, il ciclo termina.

Esempio 1: Ciclo while semplice
"""
# Esempio 1: contare da 1 a 5
numero = 1
while numero <= 5:
    print(numero)
    numero += 1  # Incrementa il numero di 1 a ogni iterazione

"""
In questo esempio, il ciclo `while` continua a stampare il valore della variabile `numero` finché 
numero è minore o uguale a 5. Ad ogni iterazione, incrementiamo `numero` di 1. Quando `numero` 
diventa 6, la condizione (numero <= 5) non è più vera, e il ciclo si interrompe.
"""

"""
Esempio 2: Ciclo infinito
"""
# Esempio 2: ciclo infinito (questo ciclo non si ferma mai)
# while True:
#     print("Questo ciclo è infinito!")
"""
Nota: Questo ciclo stampa continuamente "Questo ciclo è infinito!" perché la condizione `True`
è sempre vera. Questo tipo di ciclo può essere interrotto solo con un break manuale o con una condizione.
Non eseguire questo ciclo senza controlli, altrimenti potrebbe bloccare il programma!
"""

"""
Esempio 3: Uso di break e continue
- `break`: Interrompe il ciclo in modo immediato, anche se la condizione del `while` è ancora vera.
- `continue`: Salta l'iterazione corrente e passa alla successiva.
"""
# Esempio 3: interrompere il ciclo con `break`
numero = 1
while numero <= 10:
    print(numero)
    if numero == 5:  # Il ciclo si ferma quando il numero è 5
        break
    numero += 1

# Esempio 4: Saltare un'iterazione con `continue`
numero = 0
while numero < 5:
    numero += 1
    if numero == 3:
        continue  # Salta il numero 3 e va avanti con il ciclo
    print(numero)

"""
In sintesi:
- Il ciclo `while` viene utilizzato per eseguire un blocco di codice finché una condizione è vera.
- Si può usare `break` per uscire da un ciclo prima che la condizione diventi falsa.
- Si può usare `continue` per saltare un'iterazione e passare alla successiva.

Attenzione ai cicli infiniti: assicurati che la condizione cambi ad ogni iterazione, 
altrimenti il ciclo potrebbe non terminare mai.
"""
