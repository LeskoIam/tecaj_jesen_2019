# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.


def ime_funkcije(ime):
    """testna funkcija

    :param ime: your name
    """
    print(f"hello {ime}")


ime_funkcije("lesko")
ime_funkcije("tadej")


def sestej(a, b):
    """Sesteje dve stevili

    :param a: int
    :param b: int
    :return: obe stevilki in rezultat
    """
    rezultat = a + b
    print(rezultat)
    return [a, b, rezultat]


print(sestej(2, 3)[2] + 1)

print("konec")


def f2(a, b=5):
    return a + b


print(f2(1, 2))
print(f2(b=1, a=2))

print("-"*40)

def f3(a, b, c=23, d=43, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(d)
    print(args)
    print(kwargs)

f3(1, 2, 4, 5, 12, 13, 14, 16, 76, test=43, jaz=60, ti=666)


def f4(*args):
    funvlkd(*args)