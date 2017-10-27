weight = input("Enter your weight in kilograms")
height = input("Enter your height in meters")
weight = float(weight)
height = float(height)

bmi = weight/(height*height)

if bmi <= 18.5:
    print("im jelly u so skinny")
elif ((bmi > 18.5) and (bmi >=24.9)):
    print("ya doin good")
elif ((bmi > 25) and (bmi >=29.9)):
    print("aww dangerous ground boi")
elif bmi>30:
    print("ya need halp")


