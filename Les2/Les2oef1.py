aantal_uren_gewerkt = int(input("Hoeveel uur heb je deze maand gewerkt? "))
uurloon = 8.5
maandloon = aantal_uren_gewerkt * uurloon 
if aantal_uren_gewerkt > 20:
    print("proficiat, je krijgt een premie van 25 euro")
    maandloon += 25
print("je verdient deze maand " + str(maandloon) + " euro")