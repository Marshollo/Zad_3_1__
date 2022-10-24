# kalkulator

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
dzielenie = num1 / num2

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
