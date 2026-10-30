kostprijs_zonnepanelen = float(input("hoeveel euro betaalde je voor je zonnenpanelen? "))
terugkrijgen = kostprijs_zonnepanelen * 0.20 
if terugkrijgen < 600:print("je krijgt een premie van " + str(round(terugkrijgen, 2)) + " euro")
if terugkrijgen > 600:
  print("je krijgt een premie van 600 euro")