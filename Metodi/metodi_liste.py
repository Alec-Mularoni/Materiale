# Definizione di una lista di esempio
mia_lista = [10, 20, 30, 40, 50]

# 1. append() - Aggiunge un elemento alla fine della lista
mia_lista.append(60)
# Ora mia_lista è [10, 20, 30, 40, 50, 60]

# 2. extend() - Aggiunge tutti gli elementi di un'altra lista alla fine
mia_lista.extend([70, 80])
# Ora mia_lista è [10, 20, 30, 40, 50, 60, 70, 80]

# 3. insert() - Inserisce un elemento in una posizione specifica
mia_lista.insert(1, 15)  # Inserisce 15 alla posizione 1
# Ora mia_lista è [10, 15, 20, 30, 40, 50, 60, 70, 80]

# 4. remove() - Rimuove il primo elemento uguale al valore specificato
mia_lista.remove(30)
# Ora mia_lista è [10, 15, 20, 40, 50, 60, 70, 80]

# 5. pop() - Rimuove e restituisce l'ultimo elemento (o quello in una posizione specifica)
ultimo = mia_lista.pop()  # Rimuove e restituisce l'ultimo elemento (80)
# Ora mia_lista è [10, 15, 20, 40, 50, 60, 70]

# 6. index() - Restituisce l'indice della prima occorrenza di un elemento
indice_40 = mia_lista.index(40)
# indice_40 sarà 3

# 7. count() - Restituisce il numero di volte che un elemento appare nella lista
conta_20 = mia_lista.count(20)
# conta_20 sarà 1 (20 appare una sola volta)

# 8. sort() - Ordina la lista in modo crescente (modifica la lista in-place)
mia_lista.sort()
# Ora mia_lista è [10, 15, 20, 40, 50, 60, 70]

# 9. reverse() - Inverte l'ordine degli elementi nella lista
mia_lista.reverse()
# Ora mia_lista è [70, 60, 50, 40, 20, 15, 10]

# 10. clear() - Rimuove tutti gli elementi dalla lista
mia_lista.clear()
# Ora mia_lista è []

