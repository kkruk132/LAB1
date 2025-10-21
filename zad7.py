#Zad 7


#Wczytywanie zmiennych od użytkownika
a = float(input("Podaj zmienną A: "))
b = float(input("Podaj zmienną B: "))

#Sprawdzenie zmiennych i obliczenia
if a == 0 and b == 0:
    print("Równanie ma nieskończenie wiele rozwiązań")
elif a == 0 and b != 0:
    print("Równanie sprzeczne")
elif a != 0:
     x = -b / a
     print("Wynik to x=",x)