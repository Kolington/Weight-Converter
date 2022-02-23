weight = int(input('Enter your Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"Your Weight is {converted} kilos")
else:
    converted = weight / 0.45
    print(f"Your Weight is {converted} pounds")
