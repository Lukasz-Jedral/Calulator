import sys
import logging
logging.basicConfig(level=logging.DEBUG)

def calc_2_numbers():
    '''Użytkownik będzie poproszony o wybranie rodzaju działania i podanie dwóch liczb.
    Funkcja zwróci wynik działania'''

    calculation_type = input("Podaj działanie, posługując się odpowiednią liczbą:\n"\
                             + "1 - Dodawanie\n"\
                             + "2 - Odejmowanie\n"\
                             + "3 - Mnożenie\n"\
                             + "4 - Dzielenie:\n")
    if calculation_type == '1' or calculation_type == '2'\
    or calculation_type == '3' or calculation_type == '4':
        pass
    else:   #ograniczenie wprowadanych wartosci do 1,2,3,4
        print("Dozwolone są jedynie wartości od 1 do 4. Zamykam program.")
        return

    user_value1 = input("Podaj pierwszą liczbę:")
    user_value2 = input("Podaj drugą liczbę:")

    try: #kontrola czy podane wartosci sa liczbami
        number1 = float(user_value1)
        number2 = float(user_value2)
    except:
        print("Przynajmniej jedna z podanych wartości nie jest liczbą. Zamykam program.")
        return

    if calculation_type == '1':
        calculation_result = number1 + number2
        calculation_name = "Dodaję"
    if calculation_type == '2':
        calculation_result = number1 - number2
        calculation_name = "Odejmuję"
    if calculation_type == '3':
        calculation_result = number1 * number2
        calculation_name = "Mnożę"
    if calculation_type == '4':
        if number2 == 0.0:
            print("Dzielenie przez zero niemożliwe. Zamykam program")
            return
        else:
            calculation_result = number1 / number2
            calculation_name = "Dzielę"

    logging.info(f"{calculation_name}: {number1} i {number2}")
    logging.info(f"Wynik: {calculation_result}")
    return calculation_result

if __name__ == "__main__":
    calc_2_numbers()

