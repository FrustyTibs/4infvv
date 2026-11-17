from random import randrange
random_getal1 = (randrange(10) + 1)
random_getal2 = (randrange(10) + 1)
maal_oefening_invullen = int(input("Hoeveel is " + str(random_getal1) + " maal " + str(random_getal2 ) + "? "))
maal_oefening = random_getal1 * random_getal2
if maal_oefening_invullen == maal_oefening:
    print("correct, het Antwoord was " + str(maal_oefening))
else:
    print("jammer, het antwoord was " + str(maal_oefening))