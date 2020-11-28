# Pytanie 9 - dla danego stringa x stwórz słownik
# przechowujący informację ile razy dana litera wystąpiła w stringu

x = "myszydokazujągdykotanieczują"

D = {}                   # tworzenie pustego słownika
for litera in x:         # dla kolejnej litery w stringu x
    if litera not in D:  # jeśli litera nie znajduje się w słowniku D
        D[litera] = 1    # stwórz nowy klucz 'litera' w D i przypisz mu wartość 1
    else:                # w przeciwnym wypadku (klucz już istnieje)
        D[litera] += 1   # zwiększ wartość pod kluczem o 1 (D[litera] += 1 to zapis równoważny do D[litera] = D[litera] + 1)
print(D)                 # wydrukuj słownik D

# zadanie dodatkowe
S = {x:x+1 for x in range(10000) if x%23 == 0}

# sposób 1
if 7430 in S.keys():
    print(True)
else:
    print(False)

# sposób 2
print(True if 7430 in S.keys() else False)
