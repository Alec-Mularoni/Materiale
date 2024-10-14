import os
pw ="ciao"
ins = ""
tentativi = 0
num_max_tentativi = 3

while ins != pw:
    if tentativi == num_max_tentativi:
        print("Numero massimo di tentativi raggiunto")
        break
    tentativi += 1
    ins = input("inserisci una pw:")


    