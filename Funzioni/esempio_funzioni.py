var1=2
var2=7

var1 =3
def add():
    somma=var1+var2
    return somma

def add_with_arg(arg1, arg2="ciao"):
    somma = arg1 + arg2
    return somma

add()
print(add_with_arg(2,7))
risultato = add_with_arg(29, 1)
print(risultato)

