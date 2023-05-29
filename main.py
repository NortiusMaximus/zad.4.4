import logging
logging.basicConfig(level=logging.DEBUG)

def suma(l):
    logging.info(f'Dodaję do siebie liczby z listy {l}')
    print(f'Wynik to {sum(l)}')

def roznica(x, y):
    logging.info(f'Odejmuję {y} od {x}')
    print(f'Wynik to {x - y}')

def mnozenie(l):
    wynik = 1
    logging.info(f'Mnożę przez siebie liczby z listy {l}')
    for x in l:
        wynik = wynik * x
    print(f'Wynik to {wynik}')

def dzielenie(x, y):
    logging.info(f'Dzielę {x} przez {y}')
    print(f'Wynik to {x / y}')

if __name__ == "__main__":
    dzialanie = float(input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: '))
    pierwsza = float(input('Podaj pierwszą liczbę: '))
    druga = float(input('Podaj drugą liczbę: '))

    if dzialanie == 1:
        wiecej = [pierwsza, druga] + list(map(float, input("Możesz wprowadzić dodatkowe składniki sumy, oddzielaj je spacją: ").split()))
        suma(wiecej)
    elif dzialanie == 2:
        roznica(pierwsza, druga)
    elif dzialanie == 3:
        wiecej = [pierwsza, druga] + list(map(float, input("Możesz wprowadzić dodatkowe składniki mnożenia, oddzielaj je spacją: ").split()))
        mnozenie(wiecej)
    elif dzialanie == 4:
        dzielenie(pierwsza, druga)
    else:
        print("Nie mam takiego działania")
        exit(1)