import sys
argumenty=sys.argv[1:]
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
    while not wybor_opcji == "4":
        print("Opcje :\n 1. uczeń\n 2. nauczyciel\n 3. wychowawca\n 4. koniec)")

        klasy={
            "2B":{"wychowawca": None,"uczniowie":[], "nauczyciele":[]}
                  }

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
                    if grupa =="":
                        pusty_input=True
                    grupy.append(grupa)
                nowy_nauczyciel=Nauczyciel(imie_nauczyciela_input=imie_nauczyciela_input, przedmiot_input=przedmiot_input,grupy=grupy)
                for grupa in grupy:
                    klasy[grupa]["nauczyciele"].append(nowy_nauczyciel)
                klasy[grupa]={"wychowawca":None, "uczniowie":[], "nauczyciele":[]}


        elif wybor_opcji=="3":
                imie_wychowawcy_input=input("Podaj imie i nazwisko wychowawcy: ")
                grupy_wychowawcy=[]
                pusty_input = False
                while not pusty_input:
                    klasy_input = input("Podaj nazwe klasy: ")
                    nowy_wychowawca = Wychowawca(imie_wychowawcy_input=imie_wychowawcy_input, klasy_input=klasy_input)
                    for klasy_input in grupy_wychowawcy:
                        klasy[klasy_input]["wychowawca"].append(nowy_wychowawca)
                    klasy[klasy_input] = {"wychowawca": None, "uczniowie": [], "nauczyciele": []}

                    if klasy_input == "":
                        pusty_input = True







        elif wybor_opcji== "4":
            pass

        else:
            print("Brak podanej opcji.")
