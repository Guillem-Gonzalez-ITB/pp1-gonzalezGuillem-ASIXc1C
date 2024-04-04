import string
import systemColors
import unicodedata
import main

MENU = ["1 - Lletres - Quantitat",
        "2 - Lletres - Vocals i consonants",
        "3 - Text - Codificar",
        "4 - Text - Destacar vocals",
        "5 - Executar totes les utilitats",
        "6 - Sortir de l'aplicació"]


def showmenu():
        for n in range(0, len(MENU)):
                print(str(MENU[n]))


def optionget():
        try:
                opcio = int(input("a"))
        except:
                print("Error: Escriu un nombre del 1 al 5")
                return optionget()
        return datacheck(opcio)

def datacheck(option):
        if 1 > option > 5:
                print("Error: escull una opció del 1 al 5")
                return optionget()
        else:
                return optionselect(option)


def optionselect(option):
        if option == 1:
                return manyletters()
        elif option == 2:
                return whichletters()
        elif option == 3:
                return textcode()
        elif option == 4:
                return vowelhighlight()
        elif option == 5:
                return runall()
        else:
                exit()


def stringget():
        text = input()
        return text


def manyletters():
        lletres = 0
        textnormal = unicodedata.normalize(__unistr=stringget(), __form='NFC')
        for character in textnormal:
                if character in string.ascii_letters:
                        lletres += 1

        print("De", len(textnormal), "caràcters", lletres, "són lletres.")
        return(main.main())


def whichletters:
        text = stringget()
        lletra = []
        quantitat = []
        posicio = []

        for letter in text:
                if letter in lletra:
                        posicio.append()


def textcode():


def vowelhighlight():


def runall():