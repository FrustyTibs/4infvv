getal1 = float(input("geef het eerste getal in "))
getal2= float(input("geef het tweede getal in "))
bewerking = input("geef de bewerking in (+, -, *, /) ")
if bewerking == "+":
  print("De som is " + str(round(getal1+getal2, 2) ))
if bewerking == "/":
  print("het quotiënt is " + str(round(getal1/getal2, 2)))
if bewerking == "*":
  print("het product is " + str(round(getal1*getal2, 2)))
if bewerking == "-":
  print("het verschil is " + str(round(getal1-getal2, 2)))