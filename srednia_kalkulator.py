# -*- coding = UTF-8 -*-
from numpy import array
def srednia_calc(oceny,wagi):
    ocenyxwagi = []
    for i in range(len(oceny)):
        ocenyxwagi.append(oceny[i] * wagi[i])
    oceny_sum = sum(ocenyxwagi)
    wagi_sum = sum(wagi)
    srednia = oceny_sum/wagi_sum
    return srednia

def putting_input():
    oceny_string = input("""
Wypisz swoje oceny rozdzielając je przecinkami (,).
Liczby całkowite od dziesiętnych rozdzielaj kropką (przykład: 4.5):
""")
    wagi_string = input("""
Wypisz liczby ECTS za przedmioty w tej samej kolejności co przedmioty (jestem prostym programem :3):
""")
    oceny_string_list = oceny_string.split(",")
    wagi_string_list = wagi_string.split(",")
    return oceny_string_list, wagi_string_list, oceny_string, wagi_string



if __name__ == '__main__':
    print("""
Kalkulator średniej do stypendium rektorskiego v0.2c
by michalkowalski94 || https://github.com/michalkowalski94

!!!Pamiętaj aby nie używać spacji przy wykonywaniu poniższych poleceń!!!

""")
    oceny_string_list, wagi_string_list, oceny_string, wagi_string = putting_input()
    while len(oceny_string_list) != len(wagi_string_list) or (len(oceny_string) == 0 and len(wagi_string) == 0):
        if len(oceny_string_list) < len(wagi_string_list):
            print("Nie równa ilość ocen i ETCS, prawdopodobnie przeoczyłeś/łaś oceny")
            oceny_string_list, wagi_string_list, oceny_string, wagi_string = putting_input()
        elif len(oceny_string_list) > len(wagi_string_list):
            print("Nie równa ilość ocen i ETCS, prawdopodobnie przeoczyłeś/łaś ECTSy")
            oceny_string_list, wagi_string_list, oceny_string, wagi_string = putting_input()
        elif len(oceny_string) == 0:
            print("Nie podano ocen")
            oceny_string_list, wagi_string_list, oceny_string, wagi_string = putting_input()
        elif len(wagi_string) == 0:
            print("Nie podano ECTS")
            oceny_string_list, wagi_string_list, oceny_string, wagi_string = putting_input()
            
    oceny = [float(oceny_string_list[i]) for i in range(len(oceny_string_list))]
    wagi = [float(wagi_string_list[i]) for i in range(len(oceny_string_list))]
    oceny_array = array(oceny)
    wagi_array = array(wagi)
    srednia = srednia_calc(oceny_array,wagi_array)
    print("Twoja średnia wynosi dokładnie: %s" %srednia)
    input("Naciśnij enter aby zakończyć działanie programu")
