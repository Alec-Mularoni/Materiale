# Definizione di una stringa di esempio
mia_stringa = "Ciao, come stai?"

# 1. lower() - Restituisce la stringa in minuscolo
minuscolo = mia_stringa.lower()
# minuscolo sarà "ciao, come stai?"

# 2. upper() - Restituisce la stringa in maiuscolo
maiuscolo = mia_stringa.upper()
# maiuscolo sarà "CIAO, COME STAI?"

# 3. strip() - Rimuove spazi o caratteri specifici all'inizio e alla fine della stringa
pulita = mia_stringa.strip()
# pulita sarà "Ciao, come stai?" (se ci fossero spazi ai margini, sarebbero rimossi)

# 4. replace() - Sostituisce una sottostringa con un'altra
nuova_stringa = mia_stringa.replace("Ciao", "Salve")
# nuova_stringa sarà "Salve, come stai?"

# 5. split() - Divide la stringa in una lista di parole basata su un delimitatore
parole = mia_stringa.split()
# parole sarà ['Ciao,', 'come', 'stai?']

# 6. join() - Unisce una lista di stringhe in una singola stringa con un separatore
unita = " ".join(parole)
# unita sarà "Ciao, come stai?"

# 7. find() - Restituisce l'indice della prima occorrenza di una sottostringa, -1 se non trovata
posizione = mia_stringa.find("come")
# posizione sarà 6 (indice di inizio della parola "come")

# 8. startswith() - Verifica se la stringa inizia con una sottostringa
inizia_con = mia_stringa.startswith("Ciao")
# inizia_con sarà True

# 9. endswith() - Verifica se la stringa finisce con una sottostringa
finisce_con = mia_stringa.endswith("?")
# finisce_con sarà True

# 10. isdigit() - Verifica se la stringa contiene solo cifre
solo_numeri = mia_stringa.isdigit()
# solo_numeri sarà False (la stringa contiene lettere e spazi)
