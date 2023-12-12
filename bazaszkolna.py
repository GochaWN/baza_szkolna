import sys

class Uczen:
    def __init__(self, imie_i_nazwisko_input, klasa_input):
        self.imie_i_mazwisko = imie_i_nazwisko_input
        self.klasa = klasa_input

class Nauczyciel:
    def __init__(self, imie_nauczyciela_input, przedmiot_input, grupy):
        self.imie_nauczyciela=imie_nauczyciela_input
        self.przedmiot=przedmiot_input
        self.grupy=grupy

class Wychowawca:
    def __init__(self,imie_wychowawcy_input, klasy_input):
        self.imie_wychowawcy=imie_wychowawcy_input
        self.klasy=klasy_input



print("Witaj w programie bazy szkolnej.")
wybor_opcji = []
klasy = {
    "2B": {"wychowawca": None, "uczniowie": [], "nauczyciele": []}
}


while not wybor_opcji == "4":

    print("Opcje :\n 1. uczeń\n 2. nauczyciel\n 3. wychowawca\n 4. koniec)")



    wybor_opcji=input("Podaj numer opcji ktora chesz wykonac:")


    if wybor_opcji == "1":
        print("Dodaj ucznia")
        imie_i_nazwisko_input=input("Podaj imie i nazwisko ucznia: ")
        klasa_input= input("Podaj klase ucznia: ")
        nowy_uczen=Uczen(imie_i_nazwisko_input=imie_i_nazwisko_input,klasa_input=klasa_input)
        if klasa_input not in klasy:
            klasy[klasa_input]={"wychowawca":None, "uczniowie":[], "nauczyciele":[]}
            klasy[klasa_input]["uczniowie"].append(nowy_uczen)


    elif wybor_opcji == "2":
            imie_nauczyciela_input=input("Podaj imie i nazwisko nauczyciela: ")
            przedmiot_input=input("Podaj nazwę przedmiotu prowadzonego: ")
            grupy=[]
            pusty_input=False
            while not pusty_input:
                grupa = input("Podaj nazwe klasy: ")
                if not grupa:
                    break
                grupy.append(grupa)
            nowy_nauczyciel=Nauczyciel(imie_nauczyciela_input=imie_nauczyciela_input, przedmiot_input=przedmiot_input,grupy=grupy)
            for grupa in grupy:
                if grupa not in klasy:
                    klasy[grupa] = {"wychowawca": None, "uczniowie": [], "nauczyciele": []}
            klasy[grupa]["nauczyciele"].append(nowy_nauczyciel)



    elif wybor_opcji=="3":
            imie_wychowawcy_input=input("Podaj imie i nazwisko wychowawcy: ")
            grupy_wychowawcy=[]

            klasy_input = input("Podaj nazwe klasy: ")

            nowy_wychowawca = Wychowawca(imie_wychowawcy_input=imie_wychowawcy_input, klasy_input=klasy_input)
            #imie_wychowawcy_input=imie_wychowawcy_input, klasy_input=klasy_input
            for klasy_input in grupy_wychowawcy:
                if klasy_input not in klasy:
                    klasy[klasy_input] = {"wychowawca": None, "uczniowie": [], "nauczyciele": []}
                    klasy[klasy_input]["wychowawca"].append(nowy_wychowawca)


    elif wybor_opcji== "4":
        print ("Program zakonczony. Podaj w terminalu argument ktory chcesz wykonac.")

    else:
        print("Brak podanej opcji.")

phrase=sys.argv[1]

if phrase in klasy:
    klasa=klasy[phrase]
    wychowawca= klasy["wychowawca"]
    uczniowie= klasa["uczniowie"]

    print(f"Klasa:{phrase}")
    print(f"Wychowawca:{wychowawca.imie_wychowawcy}")
    for uczen in uczniowie:
        print(f"Uczen:{uczen.imie_i_mazwisko}")

if phrase in imie_wychowawcy_input:
    imie_wychowawcy_input=imie_wychowawcy_input[phrase]
    uczniowie=klasa["uczniowie"]

    print(f"Wychowawca:{phrase}")
    for uczen in uczniowie:
        print(f"Uczen:{uczen.imie_i_mazwisko}")

if phrase in imie_nauczyciela_input:
    imie_nauczyciela_input=imie_nauczyciela_input[phrase]
    wychowawca=klasy["wychowawca"]

    print(f"Nauczyciel:{phrase}")
    for grupa in klasa_input:
        print(f"Wychowawcy:{imie_wychowawcy_input}")

if phrase is imie_i_nazwisko_input:
    imie_i_nazwisko_input=imie_i_nazwisko_input[phrase]
    nauczyciel=klasa_input["nauczyciel"]
    przedmiot_input=przedmiot_input["przedmiot"]

    print(f"Uczen:{phrase}")
    for uczen in uczniowie:
        print(f"Przedmioty :{przedmiot_input}")
        print(f"Nauczyciel prowadzacy przedmiot:{nauczyciel}")

else:
    print("Error")
