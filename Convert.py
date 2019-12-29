print("Welcome to Python weight converter")
weight = input("Please input your weight: ")
weight_type: str = input("What Type (L)bs or (K)g?")
if weight_type.upper() == "K":
    print(f" You are {round(float(weight) * 2.2, 2)} Pounds..")
elif weight_type.upper() == "L":
    print(f" You are {round(float(weight) / 2.2,2)} Kilograms..")
else:
    print("invalid input type..")