def div(a,b):
    ris = 0
    try:
        ris = a/b
        return ris
    except ZeroDivisionError as e:
        print(e)
        print("Non si divide per zero")
    finally:
        return ris
    
print(div(4, 0))
print(div(4, 2))