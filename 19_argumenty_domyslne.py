# Pytanie 19 - wyjasnij jak działa poniższa funkcja.
# Wyjaśnij skąd wzięły się wyniki zwrócone przez poszczególne wywołania funkcji.

def dodaj_do_listy(n, lista=[]):  # lista=[] - argument domyślny funkcji
    lista.append(n)               # dodaj n do końca listy lista
    print(lista)

# Argument domyślny, w tym wypadku pusta lista, zostaje utworzona RAZ
# podczas definiowania funkcji i nie jest tworzona od nowa podczas kolejnych jej wywołań
# dlatego modyfikacja argumentu domyślnego podczas wywołania funkcji, spowoduje zapisanie tego stanu
# i zmodyfikowana lista trafi jako argument do kolejnego wywołania funkcji
# w którym zostanie użyty argument domyślny.

dodaj_do_listy(1)
dodaj_do_listy(2,[4,5])
dodaj_do_listy(3)

# materiały doatkowe
def append_to(element, to=None):
    if to is None:
        to = []
    to.append(element)
    return to


my_list = append_to(12)
print(my_list)

my_other_list = append_to(42)
print(my_other_list)

# quiz - co zostanie wyświetlone po uruchomieniu kodu poniżej?
def usun_ostatni_element_listy(lista=[1, 1, 1, 1]):
    lista.pop()
    print(lista)


usun_ostatni_element_listy()
usun_ostatni_element_listy([5, 5, 5])
usun_ostatni_element_listy()

# Rozwiązanie:
# Pierwsze wywołanie funkcji usun_ostatni_element_listy nie ma podanego argumentu, zatem zostanie użyty argument domyślny - lista = [1, 1, 1, 1].
# Użycie na niej metody .pop() spowoduje usunięcie ostatniego elementu i wydrukowana zostanie lista [1, 1, 1].
# W ten sposób trwale została zmodyfikowana przechowywana w pamięci lista będąca argumentem domyślnym!
#
# Drugie wywołanie funkcji usun_ostatni_element_listy dostaje jako parametr listę [5, 5, 5], skraca ją o jeden element i drukuje [5, 5].
# Trzecie wywołanie funkcji usun_ostatni_element_listy ponownie sięga do listy będącej argumentem domyślnym, ale tym razem jest to już lista skrócona - zatem zawiera elementy [1, 1, 1].
# Po ponownym wywołaniu na niej metody .pop() lista zostaje ponownie skrócona i w rezultacie program drukuje [1, 1].
#
# Podsumowując, wydrukowane zostanie:
# [1, 1, 1]
# [5, 5]
# [1, 1]
