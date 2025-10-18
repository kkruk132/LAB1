# Zadanie 6 B


# Importowanie biblioteki random
import random


# Zmienna spalanie pobiera od użytkownika dane i zmienia je na float (liczby rzeczywiste)
spalanie = float(input("podaj spalanie swojego samochodu w L/100km: "))

# Modyfikacja skryptu z zad 6 dodająca pobieranie od użytkownika ceny i generowanie losowe drogi od 1 do 1000
cena = float(input("podaj aktualną cenę paliwa za litr: "))
dystans = random.randint(1, 1000)

# Obliczenie zużycia paliwa:
zuzycie = round((spalanie / 100) * dystans, 2)

# Obliczanie kosztów podróży:
koszt = round(zuzycie * 6.5, 2)
# Round wyświetla wyniki do dwóch miejsc po przecinku

# Wyświetlenie wyników wykorzystując formatowany łańcuch tekstowy, ze zmienną wstawioną w nawias klamerkowy
print(f'Twój samochód spali {zuzycie} L paliwa \nKoszt podróży wyniesie {koszt} zł\nwygenerowany dystans to {dystans} km')