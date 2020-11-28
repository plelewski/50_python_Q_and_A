# Pytanie 4 - jakiej struktury danych użyłbyś do zamodelowania
# szafki, która ma 3 szuflady, a w każdej z nich 3 przegródki?
# Stwórz taki model i umieść stringa "długopis"
# w środkowej przegródce środkowej szuflady.

szafka = [[[],[],[]],[[],[],[]],[[],[],[]]] # lista szafka zawiera trzy zagnieżdżone listy, a każda z nich kolejne trzy zagnieżdżone listy
szafka[1][1] = 'długopis'

# wpisanie stringa do środkowej listy (reprezentującej skrytkę)
# w środkowej liście (reprezentującej szufladę) w liście szafka

for a in szafka:       # pętla drukująca po kolei trzy listy będące elementami listy szafka
    print(a)


# kod dodatkowy
# Creates a list containing 5 lists, each of 8 items, all set to 0
w, h = 8, 5
Matrix = [[0 for x in range(w)] for y in range(h)]

for b in Matrix:
    print(b)
