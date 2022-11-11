import math


def zad_3_1():
    while True:
        try:
            num1 = int(input("Podaj wartość pierwszej liczby: "))
            num2 = int(input("Podaj wartość drugiej liczby: "))
            break
        except ValueError:
            print("Coś poszło nie tak. Proszę wpisać liczbę całkowitą\n")

    dodawanie = num1 + num2
    odejmowanie = num1 - num2
    mnozenie = num1 * num2
    if num2 != 0:
        dzielenie = num1 / num2
    else:
        dzielenie = "Nie dzielimy przez zero"

    while True:
        znak = (input("Podaj znak operacji: + , - , * , /\n"))

        if znak == '+':
            print("Wynik to: ", dodawanie)
            break
        elif znak == '-':
            print("Wynik to: ", odejmowanie)
            break
        elif znak == '*':
            print("Wynik to: ", mnozenie)
            break
        elif znak == '/':
            print("Wynik to: ", dzielenie)
            break
        else:
            print('\nZły znak operacji.')


def zad_3_2():
    return print("Witaj świecie")


def zad_celcius():
    """
        Ta funkcja przelicza temperature w F na temperature w C
        """
    f = eval(input("Podaj temperaturę w Fahrenheit: "))
    c = (f - 32) * (5 / 9)
    return print(("Temperatura w Celcius, wynosi: " + str(c)))


def zad_fahrenheit():
    """
    Ta funkcja przelicza temperature w C na temperature w F
    """
    c = eval(input("Podaj temperaturę w Celcius: "))
    f = (c * (9 / 5)) + 32
    return print(("Temperatura w Fahrenheit, wynosi: " + str(f)))


def pola_figur():
    y = 1
    while y:
        y = 0
        liczba = eval(input("Wybierz liczbę przypisaną do figury, której pole chcesz obliczyć\n Kwadrat = 1\n Trójkąt "
                            "= 2\n "
                            "Trójkąt równoboczny = 3\n Koło = 4\n Trapez = 5\n Prostokąt = 6\n"))
        if liczba == 1:
            kwadrat = eval(input("Podaj długość boku kwadratu: "))
            print("Pole kwadratu wynosi: " + str(kwadrat ** 2))
        elif liczba == 2:
            podst = eval(input("Podaj długość podstawy trójkąta: "))
            wysok = eval(input("Podaj długość wysokości trójkąta: "))
            print("Pole trójkąta wynosi: " + str(podst * wysok / 2))
        elif liczba == 3:
            podsta = eval(input("Podaj długość podstawy trójkąta równobocznego : "))
            print("Pole trójkąta równobocznego wynosi: " + str(podsta ** 2 * math.sqrt(3) / 4))
        elif liczba == 4:
            promien = eval(input("Podaj długość promienia koła: "))
            print("Pole koła wynosi: " + str(math.pi * promien ** 2))
        elif liczba == 5:
            podst1 = eval(input("Podaj długość pierwszej podstawy: "))
            podst2 = eval(input("Podaj długość drugiej podstawy: "))
            wysok1 = eval(input("Podaj długość wysokości trapezu: "))
            print("Pole trapezu wynosi: " + str((podst1 + podst2) * wysok1 / 2))
        elif liczba == 6:
            bok1 = eval(input("Podaj długość pierwszego boku prostokąta: "))
            bok2 = eval(input("Podaj długość drugiego boku prostokąta: "))
            print("Pole prostokąta wynosi: " + str(bok1 * bok2))

        koniec1 = eval(input("\nJeśli chcesz zakończyć wciśnij 1, jeśli chcesz uruchomić "
                             "program jeszcze raz, wciśnij 2, a więc? \n"))
        if koniec1 == 1:
            break
        if koniec1 == 2:
            y = 1


def lambd():
    a1 = eval(input("Podaj pierwszą liczbę do wyliczenia kwadratu różnicy: "))
    b1 = eval(input("Podaj drugą liczbę do wyliczenia kwadratu różnicy: "))
    zm = (lambda a, b: (a - b) ** 2)(a1, b1)
    print("\nWynik to, ", zm)


def pearson():
    import numpy as gg
    a = gg.array([3, 2, 1, 0, -1])
    b = gg.array([5, 2, 4, -2, 1])
    wyn = gg.corrcoef(a, b)

    print(wyn)


############################################### uruchamianie zadań ##########################################
i = True
while i:
    i = False
    x = eval(
        input("\nWprowadź numer zadania, do wyboru: \n Zadanie 3_1 (Kalkulator) = 1\n Zadanie 3_2 (hello world) = 2\n "
              "Zadanie 3_7 (Celcius) = 3\n Zadanie 3_7 (Fahrenheit) = 4\n Zadanie "
              "3_11 (Pearson) = 5\n Zadanie 3_13 (Pola figur) = 6\n Zadanie 3_20 (lambda) = 7\n Wybierasz: "))
    if x == 1:
        zad_3_1()
    elif x == 2:
        zad_3_2()
    elif x == 3:
        zad_celcius()
    elif x == 4:
        zad_fahrenheit()
    elif x == 5:
        pearson()
    elif x == 6:
        pola_figur()
    elif x == 7:
        lambd()
    elif x == 0:
        i = False

    koniec = eval(input("\nJeśli chcesz wybrać inne zadanie naciśnij 9, jeśli chcesz zakończyć wciśnij 0, a więc? \n"))
    if koniec == 0:
        break
    if koniec == 9:
        i = True
