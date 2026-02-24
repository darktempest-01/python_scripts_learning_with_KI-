# Variables

def alter_abfrage():
    alter = int(input("Bitte geb dein Alter ein "))
    if alter >= 18:
        return  "Erwachsen"
    elif alter >= 14:
        return "Jugendlicher"
    elif alter >= 6:
        return "Kind"
    else:
        return "Kleinkind"


# Schleifen
def zählen(test_number):
    for i in range(test_number):
        print(i)


# Funktionen
def begruessen(name):
    return f"Hallo {name}!"

zählen(12)
print(begruessen("Nick"))
print(alter_abfrage())
print(input("Taste zum Beenden drücken"))
