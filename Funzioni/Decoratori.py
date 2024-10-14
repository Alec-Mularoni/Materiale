def mio_decoratore(msg):
    def wrapper():
        print("La funzione non è ancora eseguita")
        msg()
        print("La funzione è stata eseguita")
        return None
        
    return wrapper()

@mio_decoratore
def somma():
    print(10+12)

mio_decoratore(somma())
