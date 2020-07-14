import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")

def calc_2_numbers():
    calculation_type = input("Podaj działanie, posługując się odpowiednią liczbą:\n"\
                             + "1 - Dodawanie\n"\
                             + "2 - Odejmowanie\n"\
                             + "3 - Mnożenie\n"\
                             + "4 - Dzielenie:")
    if not calculation_type == 1 or calculation_type == 2\
    or calculation_type == 3 or calculation_type == 4: #ograniczenie wprowadanych wartosci do 1,2,3,4
        print("Dozwolone są jedynie wartości od 1 do 4. Zamykam program.")
        return

    number1 = input("Podaj pierwszą liczbę:")
    number2 = input("Podaj drugą liczbę:")

    if  isinstance(number1, (int, float, complex)) and not isinstance(number1, bool):
        isnumber = True
    else:
        isnumber = False
    if isinstance(number2, (int, float, complex)) and not isinstance(number2, bool):
        isnumber = True
    else:
        isnumber = False

    if isnumber = False:
        print("At least one of given values in not valid number. Function terminated")
        return





if __name__ == "__main__":
    logging.debug("The program was called with this parameters %s" % sys.argv[1:])
    logging.debug("First parameter is %s" % sys.argv[1])
    logging.debug("Second parameter is %s" % sys.argv[2])
