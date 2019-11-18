import ai
import util

def tah_hrace (pole, symbol):
    while True:
        pozice = input("Na jake pozici chces hrat? Zadej 0-19")
        int_pozice = int(pozice)
        if int_pozice >= 0 and int_pozice <= 19 and pole[int_pozice] == "-":
            return util.tah (pole, int_pozice, symbol)
        else:
            print ("Zadal jsi spatne cislo, tytyty! Styd se!")

def piskvorky1d():
    pole = "--------------------"
    while True:
        print (pole)
        pole = tah_hrace (pole, "x")
        print (pole)
        aktualni_stav = vyhodnot(pole)
        if aktualni_stav == "-":
            pole = ai.tah_pocitace (pole, "o")
            aktualni_stav = vyhodnot(pole)

        if aktualni_stav == "!":
            print ("Remiza")
            break
        elif aktualni_stav == "x":
            print ("Vyhral clovek")
            break
        elif aktualni_stav == "o":
            print ("Vyhral pocitac")
            break
    print (pole)



def vyhodnot(pole):
    if ("xxx" in pole):
        return "x"
    elif ("ooo" in pole):
        return "o"
    elif ("-" not in pole):
        return "!"
    else:
        return "-"
