import logging
logging.basicConfig(level=logging.DEBUG)

def suma(x, y):
    logging.info(f'Dodaję {x} i {y}')
    print(f'Wynik to {x + y}')

def roznica(x, y):
    logging.info(f'Odejmuję {y} od {x}')
    print(f'Wynik to {x - y}')

def mnozenie(x, y):
    logging.info(f'Mnożę {x} przez {y}')
    print(f'Wynik to {x * y}')

def dzielenie(x, y):
    logging.info(f'Dzielę {x} przez {y}')
    print(f'Wynik to {x / y}')

if __name__ == "__main__":
    dzialanie = float(input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: '))
    pierwsza = float(input('Podaj pierwszą liczbę: '))
    druga = float(input('Podaj drugą liczbę: '))

    if dzialanie == 1:
        suma(pierwsza, druga)
    elif dzialanie == 2:
        roznica(pierwsza, druga)
    elif dzialanie == 3:
        mnozenie(pierwsza, druga)
    elif dzialanie == 4:
        dzielenie(pierwsza, druga)
    else:
        print("Nie mam takiego działania")
        exit(1)