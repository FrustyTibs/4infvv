punten = int(input("Hoeveel punten heb je op de toets gehaald? "))
totaal = int(input("Op hoeveel punten stond de toets? "))
percentage = punten / totaal * 100
print("je hebt " + str(percentage) + "%.")
if percentage > 50:
    print("Proficiat, je bent geslaagd!")
if percentage < 50:
    print("Je bent niet geslaagd")
if percentage == 50:
    print("Je bent nipt door")