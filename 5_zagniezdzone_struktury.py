# Pytanie 5 - z poniższej listy wypisz stringa "schowany"

L = [[34, False], [0], [('abc', 123), {'a': 1, 'x': (True, 'schowany', 5)}]]

print(L[2][1]['x'][1])

# odczytywanie po kolei:
# L[2] zwraca: [('abc', 123), {'a': 1, 'x': (True, 'schowany', 5)}]
# L[2][1] zwraca: {'a': 1, 'x': (True, 'schowany', 5)}
# L[2][1]['x'] zwraca: (True, 'schowany', 5)
# L[2][1]['x'][1] zwraca: 'schowany'

# Zadanie dodatkowe: wypisz wróbel
K = (('król', {2:'królewna', 1: ['córka', 'wróbel']},'5'),('żółw', 'wiewiórka'))

print(K[0][1][1][1])
