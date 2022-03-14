import regex as re

imie = input("Imie: ")
if not re.match("\p{Lu}", imie):
    print("Proszę podać imię z wielkiej litery")
nazwisko = input("Nazwisko: ")
if not re.match("\p{Lu}", nazwisko):
    print("Proszę podać nazwisko z wielkiej litery")
miasto = input("Miasto: ")
if not re.match("\p{Lu}", miasto):
    print("Proszę podać miasto z wielkiej litery")
telefon = input("telefon: ")
if not re.match("[(]\d\d[)][ ]\d\d\d[-]\d\d[-]\d\d$", telefon):
    print("Format telefonu (61) 222-22-22")
kod_pocztowy = input("Kod pocztowy: ")
if not re.match("\d\d[-]\d\d\d$", kod_pocztowy):
    print("Format 11-111")

