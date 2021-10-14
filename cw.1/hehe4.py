def foo(x,y):
    return f'{x[0].capitalize()}.{y.capitalize()}'

def foo2(imie, nazwisko, fo):
    return fo(imie, nazwisko)

print (foo2("jan", "kowalski", foo))