tijd_tussen_bliksem_en_donder = int(input("Hoeveel seconden tel je tussen bliksem en donder? "))
afstand_onweer = tijd_tussen_bliksem_en_donder*343/1000
print("Het onweer is ongeveer " + str(round(afstand_onweer, 1)) + " km ver.")
if afstand_onweer <= 2:
    print("Het onweer is dichtbij. Ga snel naar binnen!")
if afstand_onweer > 2:
    print("Het onweer is ver weg, maar wees nog steeds voorzichtig")