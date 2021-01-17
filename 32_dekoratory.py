# Pytanie 32 - do czego w Pythonie służą dekoratory? Napisz dekorator, który będzie
# będzie dodawał trzy gwiazdki przed i po efekcie działania udekorowanej funkcji.

def dodaj_gwiazdki(funkcja):     # definicja dekoratora niczym nie różni się od definicji zwykłej funkcji
    def funkcja_udekorowana():   # wewnątrz dekoratowa tworzymy WEWNĘTRZNĄ funkcję, w której udekorujemy funkcję pobraną jako argument
        print("***")             # dekorowanie funkcji
        funkcja()                # wywołanie funkcji będącej argumentem dekoratora
        print("***")             # dekorowanie funkcji
    return funkcja_udekorowana   # zwrócenie funkcji WEWNĘTRZNEJ, w której udekorowano funkcję będącą argumentem dekoratora

@dodaj_gwiazdki                  # zapis @dodaj_gwiazdki BEZPOŚREDNIO nad definicją funkcji f() powoduje, że funkcja f() zostaje udekorowana
def f():                         # definicja funkcji f()
    print("Cześć, jestem f()")

f()

# zadanie dodatkowe
# 1. Co zostanie wypisane w wyniku uruchomienia poniższego kodu?
# 2. Co zostanie wypisane jeśli usuniemy linijkę 7, w której znajduje się @ wypisz_efekt_dzialania


def wypisz_efekt_dzialania(funkcja):
    def funkcja_udekorowana():
        a = funkcja()
        print(a)

    return funkcja_udekorowana


@wypisz_efekt_dzialania
def zwroc_czesc():
    return "cześć"
# odpowiedź: 1.cześć, 2. nic nie wypisze na ekran, ponieważ drukowanie jest w dekorowaniu, do którego nie dojdzie
