from faker import Faker
import random

fake = Faker()

class BaseContact:
    def __init__(self, imie_nazwisko, mail, tel):
        self.imie, self.nazwisko = imie_nazwisko.split()
        self.mail = mail
        self.tel = tel

    def contact(self):
        print(f"Wybieram numer {self.tel} i dzwonię do {self.imie} {self.nazwisko} mail: {self.mail}")

    @property
    def label_length(self):
        return len(self.imie) + len(self.nazwisko)


class BusinessContact(BaseContact):
    def __init__(self, stanowisko, firma, sluzbowy_tel, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stanowisko = stanowisko
        self.firma = firma
        self.sluzbowy_tel = sluzbowy_tel

    def contact(self):
        print(f"Wybieram numer {self.sluzbowy_tel} i dzwonię do: {self.stanowisko} {self.imie} {self.nazwisko} z firmy {self.firma}, mail: {self.mail}")

    @property
    def label_length(self):
        return len(self.imie) + len(self.nazwisko)


def create_random_contact():
    imie_nazwisko = fake.name()
    mail = fake.email()
    tel = fake.phone_number()
    return BaseContact(imie_nazwisko=imie_nazwisko, mail=mail, tel=tel)


def create_random_business_contact():
    imie_nazwisko = fake.name()
    mail = fake.email()
    tel = fake.phone_number()
    stanowisko = fake.job()
    firma = fake.company()
    sluzbowy_tel = fake.phone_number()
    return BusinessContact(imie_nazwisko=imie_nazwisko, mail=mail, tel=tel,
                           stanowisko=stanowisko, firma=firma, sluzbowy_tel=sluzbowy_tel)


Arnold = BaseContact(imie_nazwisko="Arnold Schwarzenegger", mail="A.Schwarz@mail.com", tel="342342653")
Mike = BaseContact(imie_nazwisko="Mike Mentzer", mail="Mike.Men@mail.com", tel="342345555")
Ronnie = BaseContact(imie_nazwisko="Ronnie Coleman", mail="RonnieTheKing", tel="342344444")
Franco = BaseContact(imie_nazwisko="Franco Columbu", mail="FrancoCol@mail.com", tel="34233333")
Jay = BaseContact(imie_nazwisko="Jay Cutler", mail="JayCut@mail.com", tel="342346666")

Arnold_1 = BusinessContact(stanowisko="CEO", firma="A-companion", sluzbowy_tel="342655343",
                            imie_nazwisko="Arnold Schwarzenegger", mail="A.Schwarz@mail.com", tel="342342653")
Mike_1 = BusinessContact(stanowisko="V-CEO", firma="A-companion", sluzbowy_tel="342655111",
                          imie_nazwisko="Mike Mentzer", mail="Mike.Men@mail.com", tel="342345555")
Ronnie_1 = BusinessContact(stanowisko="Członek zarządu", firma="A-companion", sluzbowy_tel="342656545",
                            imie_nazwisko="Ronnie Coleman", mail="RonnieTheKing", tel="342344444")
Franco_1 = BusinessContact(stanowisko="Członek zarządu", firma="A-companion", sluzbowy_tel="354395333",
                            imie_nazwisko="Franco Columbu", mail="FrancoCol@mail.com", tel="34233333")
Jay_1 = BusinessContact(stanowisko="Członek zarządu", firma="A-companion", sluzbowy_tel="342655999",
                         imie_nazwisko="Jay Cutler", mail="JayCut@mail.com", tel="342346666")


print(f"Arnold: {Arnold.label_length}")
print(f"Mike: {Mike.label_length}")
print(f"Ronnie: {Ronnie.label_length}")
print(f"Franco: {Franco.label_length}")
print(f"Jay: {Jay.label_length}")


print(f"Arnold_1: {Arnold_1.label_length}")
print(f"Mike_1: {Mike_1.label_length}")
print(f"Ronnie_1: {Ronnie_1.label_length}")
print(f"Franco_1: {Franco_1.label_length}")
print(f"Jay_1: {Jay_1.label_length}")


def prywatnie():
    print("Dostępni rozmówcy prywatnie:")
    print("1. Arnold")
    print("2. Mike")
    print("3. Ronnie")
    print("4. Franco")
    print("5. Jay")
    print("6. inny")

def sluzbowo():
    print("Dostępni rozmówcy służbowo:")
    print("1. Arnold_1")
    print("2. Mike_1")
    print("3. Ronnie_1")
    print("4. Franco_1")
    print("5. Jay_1")
    print("6. inny")

print("Wpisz imię osoby, do której chcesz zadzwonić!")

def calling():
    ask = input("Kontaktujesz się prywatnie czy służbowo: ")
    if ask.lower() == "prywatnie":
        prywatnie()
        wybor = input("Wybierz swojego rozmówcę: ")
        if wybor.lower() == "arnold":
            Arnold.contact()
        elif wybor.lower() == "mike":
            Mike.contact()
        elif wybor.lower() == "ronnie":
            Ronnie.contact()
        elif wybor.lower() == "franco":
            Franco.contact()
        elif wybor.lower() == "jay":
            Jay.contact()
        elif wybor.lower() == "inny":
            random_contact = create_random_contact()
            random_contact.contact()
        else:
            print("Nieznana osoba.")
    elif ask.lower() == "służbowo":
        sluzbowo()
        wybor = input("Wybierz swojego rozmówcę: ")
        if wybor.lower() == "arnold_1":
            Arnold_1.contact()
        elif wybor.lower() == "mike_1":
            Mike_1.contact()
        elif wybor.lower() == "ronnie_1":
            Ronnie_1.contact()
        elif wybor.lower() == "franco_1":
            Franco_1.contact()
        elif wybor.lower() == "jay_1":
            Jay_1.contact()
        elif wybor.lower() == "inny":
            random_business_contact = create_random_business_contact()
            random_business_contact.contact()
        else:
            print("Nieznana osoba.")
    else:
        print("Nieprawidłowy wybór. Wpisz 'prywatnie' lub 'służbowo'.")

calling()
