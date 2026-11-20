lengte = float(input("Hoe lang ben je in meter? "))
gewicht = float(input("Hoeveel weeg je in kg? "))
BMI = round(gewicht / (lengte * lengte),1)
print("Je BMI is " + str(BMI))
if BMI <18.5:
    print("categorie: ondergewicht")
elif BMI <25.5:
    print("categorie: gezond gewicht")
elif BMI <30:
    print("catgeorie: overgewicht")
elif BMI >30:
    print("categorie: zwaar overgewicht")