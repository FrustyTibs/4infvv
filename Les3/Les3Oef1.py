from datetime import date
vandaag = date.today().year
Geboortejaar = int(input("In welk jaar ben je geboren? "))

Leeftijd = vandaag - Geboortejaar
print("dit jaar word je " + str(Leeftijd) + " jaar.")
if Leeftijd <12:
    print("Je mag naar films voor alle leeftijden.")
elif Leeftijd <=15:
    print("Je mag naar films vanaf 12 jaar.")
elif Leeftijd <=17:
    print("Je mag naar films vanaf 16 jaar.")
elif Leeftijd >18:
    print("Je mag naar alle films.")