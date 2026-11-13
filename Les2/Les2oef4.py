from random import randrange
random_getal = (randrange(10) + 1)
gekozen_getal = int(input("Raad een getal van 1 tot 10: "))
if gekozen_getal == random_getal:
    print("Gewonnen! Het getal was " + str(random_getal))
else:
    print("Helaas! Het getal was " + str(random_getal))
