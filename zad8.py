#Zad 8


#Wczytywanie zmiennych od użytkownika
a = float(input("Podaj zmienną A: "))
b = float(input("Podaj zmienną B: "))
c = float(input("Podaj zmienną C: "))

#Sprawdzenie zmiennych i obliczenia
if a == 0:
    print("Nie jest to funkcja kwadratowa")
elif a != 0:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Równanie nie ma rozwiązań rzeczywistych")
    elif delta == 0:
        x = -b / (2 * a)
        print("Wynik to x=",x)
    elif delta != 0:
        x1 = (-b - delta ** 0.5) / (2 * a)
        x2 = (-b + delta ** 0.5) / (2 * a)
        print("Wynik to x1=",x1,"x2=",x2)
