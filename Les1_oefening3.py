Aantal_taakjes_uitgevoerd = int(input("Hoeveel taakjes heeft Lio uitgevoerd "))
Aantal_keer_tafel_niet_afgeruimt = int(input("Hoeveel keer heeft Lio de tafel niet afgeruimd "))
effectief_zakgeld = 5 + Aantal_taakjes_uitgevoerd * 2 - Aantal_keer_tafel_niet_afgeruimt
print(f"Lio krijgt {int(effectief_zakgeld)} euro zakgeld")