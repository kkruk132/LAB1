# Zad 6


# Zmienne dystans i spalanie pobierają od użytkownika dane i zmieniają je na float
dystans = float(input("podaj liczbę pokonanych kilometrów: "))
spalanie = float(input("podaj spalanie swojego samochodu w L/100km: "))

# Obliczenie zużycia paliwa:
zuzycie = round((spalanie / 100) * dystans, 2)

# Obliczanie kosztów podróży:
koszt = round(zuzycie * 6.5, 2)
# Round wyświetla wyniki do dwóch miejsc po przecinku

# Wyświetlenie wyników
print("Twój samochód spali",zuzycie,"L paliwa","\nKoszt podróży wyniesie",koszt,"zł")