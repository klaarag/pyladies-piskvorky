import util
from random import randrange


def tah_pocitace (pole, symbol):
    if pole.find("x-x") != -1:
        pozice = pole.find("x-x")
        return util.tah (pole, pozice + 1, symbol)

    elif pole.find("-x-") != -1:
        pozice = pole.find("-x-")
        return util.tah (pole, pozice, symbol)

    elif pole.find("xx-") != -1:
        pozice = pole.find("xx-")
        return util.tah (pole, pozice + 2, symbol)

    elif pole.find("-xx") != -1:
        pozice = pole.find("-xx")
        return util.tah (pole, pozice, symbol)

    else:
        while True:
            pozice = randrange(0, 19)
            if pole[pozice] == "-":
                return util.tah (pole, pozice, symbol)
