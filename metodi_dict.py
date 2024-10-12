# Definizione di un dizionario di esempio
mio_dizionario = {'nome': 'Mario', 'eta': 30, 'città': 'Roma'}

# 1. keys() - Restituisce tutte le chiavi del dizionario
chiavi = mio_dizionario.keys()
# chiavi sarà dict_keys(['nome', 'eta', 'città'])

# 2. values() - Restituisce tutti i valori del dizionario
valori = mio_dizionario.values()
# valori sarà dict_values(['Mario', 30, 'Roma'])

# 3. items() - Restituisce una lista di tuple (chiave, valore)
elementi = mio_dizionario.items()
# elementi sarà dict_items([('nome', 'Mario'), ('eta', 30), ('città', 'Roma')])

# 4. get() - Restituisce il valore associato a una chiave, None se non esiste
eta = mio_dizionario.get('eta')
# eta sarà 30

# 5. pop() - Rimuove e restituisce il valore associato a una chiave
città = mio_dizionario.pop('città')
# città sarà 'Roma', e ora il dizionario è {'nome': 'Mario', 'eta': 30}

# 6. update() - Aggiorna il dizionario con un altro dizionario o con coppie chiave-valore
mio_dizionario.update({'eta': 31, 'paese': 'Italia'})
# Ora mio_dizionario è {'nome': 'Mario', 'eta': 31, 'paese': 'Italia'}

# 7. clear() - Rimuove tutti gli elementi dal dizionario
mio_dizionario.clear()
# Ora mio_dizionario è {}

# 8. setdefault() - Restituisce il valore di una chiave, o la imposta con un valore predefinito se non esiste
mio_dizionario.setdefault('professione', 'Ingegnere')
# Ora mio_dizionario è {'professione': 'Ingegnere'}

# 9. copy() - Restituisce una copia superficiale del dizionario
nuovo_dizionario = mio_dizionario.copy()
# nuovo_dizionario sarà una copia di mio_dizionario

# 10. fromkeys() - Crea un nuovo dizionario con chiavi da un iterable e un valore predefinito
chiavi = ['a', 'b', 'c']
nuovo_diz = dict.fromkeys(chiavi, 0)
# nuovo_diz sarà {'a': 0, 'b': 0, 'c': 0}
