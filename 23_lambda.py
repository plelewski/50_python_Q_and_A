# Pytanie 23 - czym jest lambda?
# Napisz przykładowy kod wykorzystujący lambdę.

# lambda argument : wyrażenie
# lambda x:x+2

L = [('Anna',82), ('Robert',33), ('Artur',40), ('Feliks',56)]
# W poniższej linijce funkcja sorted pobiera sekwencję danych do posortowania i klucz, po którym będzie sortować.
# Sekwencją jest lista L, a kluczem lambda, która dla kolejnego elementu listy L (czyli tupli)
# zwraca drugi element danej tupli.
L_posortowana = sorted(L, key = lambda x:x[1])
print(L_posortowana)

# zadanie dodatkowe 1 ze stackoverflow
mult3 = filter(lambda x: x % 3 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print(list(mult3))

# zadamie dodatkowe
# Posortuj podaną listę stringów jako kryterium sortowania przyjmując ostatnią literę każdego stringa.
# Użyjemy w tym celu lambdy, która dla kolejnego elementu listy S - oznaczonego małą literą s - będzie zwracać ostatni znak danego stringa odczytany przy użyciu zapisu: s[-1].

S = ['Anna_z', 'Robert', 'Artur', 'Feliks']
S_posortowana = sorted(S, key=lambda s: s[-1])
print(S_posortowana)
