

def foo(x):
    li = ["poniedzialek", "wtorek", "sroda", "czwartek", "piatek", "sobota", "niedziela"]
    return li[(x-1)%7]

print(foo(13))