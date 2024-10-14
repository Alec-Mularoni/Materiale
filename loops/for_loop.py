"""
FOR LOOP IN PYTHON

Il ciclo `for` in Python viene utilizzato per iterare su una sequenza (come una lista, una stringa, un range).
È utile quando si sa esattamente quante volte eseguire il ciclo, o si desidera iterare su ogni elemento di una collezione.

Sintassi di base:

for variabile in sequenza:
    # blocco di codice da eseguire per ogni elemento della sequenza

- `variabile`: ad ogni iterazione, assume il valore dell'elemento corrente della sequenza.
- `sequenza`: può essere una lista, una stringa, un range, o qualsiasi oggetto iterabile.

Esempio 1: Iterare su una lista
"""
# Esempio 1: ciclo `for` su una lista
frutti = ["mela", "banana", "ciliegia"]
for frutto in frutti:
    print(frutto)

"""
In questo esempio, il ciclo `for` prende ogni elemento dalla lista `frutti`, lo assegna alla variabile `frutto`,
e stampa il valore di `frutto` ad ogni iterazione.
"""

"""
Esempio 2: Iterare su una stringa
"""
# Esempio 2: ciclo `for` su una stringa
parola = "Python"
for lettera in parola:
    print(lettera)

"""
Qui, il ciclo `for` itera su ogni carattere della stringa "Python" e stampa ogni lettera separatamente.
"""

"""
Esempio 3: Utilizzo della funzione `range()`
La funzione `range()` genera una sequenza di numeri interi. Viene spesso utilizzata per iterare un numero fisso di volte.

Sintassi:
- `range(stop)`: genera i numeri da 0 fino a `stop-1`.
- `range(start, stop)`: genera i numeri da `start` fino a `stop-1`.
- `range(start, stop, step)`: genera i numeri da `start` a `stop-1`, incrementando di `step`.

Esempio 3: ciclo `for` con range
"""
# Esempio 3: Ciclo `for` con `range`
for i in range(5):
    print(i)

"""
In questo esempio, il ciclo `for` itera su una sequenza di numeri da 0 a 4 (range(5)).
Il ciclo termina quando raggiunge il numero 5 (escluso).
"""

"""
Esempio 4: Uso di `break` e `continue` nel ciclo `for`
- `break`: Esce dal ciclo immediatamente.
- `continue`: Salta l'iterazione corrente e passa alla successiva.
"""
# Esempio 4: uso di `break`
for numero in range(1, 10):
    if numero == 6:
        break  # Esce dal ciclo quando il numero è 6
    print(numero)

# Esempio 5: uso di `continue`
for numero in range(1, 6):
    if numero == 3:
        continue  # Salta il numero 3
    print(numero)

"""
In sintesi:
- Il ciclo `for` viene utilizzato per iterare su una sequenza (liste, stringhe, range, ecc.).
- Si può usare `break` per uscire dal ciclo prima che termini la sequenza.
- Si può usare `continue` per saltare l'iterazione corrente e passare alla successiva.

Il ciclo `for` è molto utile quando sai quante volte vuoi iterare o vuoi iterare su una collezione di elementi.
"""