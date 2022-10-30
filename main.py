# kalkulator
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
    f = eval(input("Podaj temperaturę w Fahrenheit: "))
    c = (f - 32) * (5 / 9)
    return print(("Temperatura w Celcius, wynosi: " + str(c)))


def zad_fahrenheit():
    c = eval(input("Podaj temperaturę w Celcius: "))
    f = (c * (9 / 5)) + 32
    return print(("Temperatura w Fahrenheit, wynosi: " + str(f)))


def pola_figur():
    y = 1
    while y:
        y = 0
        x = eval(input("Wybierz liczbę przypisaną do figury, której pole chcesz obliczyć\n Kwadrat = 1\n Trójkąt = 2\n "
                       "Trójkąt równoboczny = 3\n Koło = 4\n Trapez = 5\n Prostokąt = 6\n"))
        if x == 1:
            kwadrat = eval(input("Podaj długość boku kwadratu: "))
            print("Pole kwadratu wynosi: " + str(kwadrat ** 2))
        if x == 2:
            podst = eval(input("Podaj długość podstawy trójkąta: "))
            wysok = eval(input("Podaj długość wysokości trójkąta: "))
            print("Pole trójkąta wynosi: " + str(podst * wysok / 2))
        if x == 3:
            podsta = eval(input("Podaj długość podstawy trójkąta równobocznego : "))
            print("Pole trójkąta równobocznego wynosi: " + str(podsta ** 2 * math.sqrt(3) / 4))
        if x == 4:
            promien = eval(input("Podaj długość promienia koła: "))
            print("Pole koła wynosi: " + str(math.pi * promien ** 2))
        if x == 5:
            podst1 = eval(input("Podaj długość pierwszej podstawy: "))
            podst2 = eval(input("Podaj długość drugiej podstawy: "))
            wysok1 = eval(input("Podaj długość wysokości trapezu: "))
            print("Pole trapezu wynosi: " + str((podst1 + podst2) * wysok1 / 2))
        if x == 6:
            bok1 = eval(input("Podaj długość pierwszego boku prostokąta: "))
            bok2 = eval(input("Podaj długość drugiego boku prostokąta: "))
            print("Pole prostokąta wynosi: " + str(bok1 * bok2))

        quit = eval(input("\nJeśli chcesz zakończyć wciśnij 1, jeśli chcesz uruchomić "
                          "program jeszcze raz, wciśnij 2, a więc? "))
        if quit == 1:
            break
        if quit == 2:
            y = 1

pola_figur()
def lambd():
    wyrazenie = lambda a, b: (a - b) ** 2
    zm = wyrazenie(6,8)
    print(zm)
