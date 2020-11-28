# Pytanie 18 - napisz funkcję, która będzie pobierać dwie liczby
# i sprawdzać czy pierwsza z nich jest podzielna przez drugą

def sprawdz_podzielnosc(a, b):
    return(a % b == 0)    # zwróć wartość logiczną wyrażenia: reszta z dzielenia a przez b wynosi 0

print(sprawdz_podzielnosc(10, 5))
print(sprawdz_podzielnosc(10, 3))
print(sprawdz_podzielnosc(1000, 7))

# zadanie dodatkowe
# Sprawdź czy liczba a jest podzielna przez b. Jeśli tak - wypisz True, jeśli nie - False.

a = 123454321
b = 11111

print(True if a%b == 0 else False)
