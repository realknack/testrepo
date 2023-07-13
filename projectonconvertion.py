weight = input('Weight: ')
unit = input('(L)bs or (K)g: ')

if unit.upper() == "K":
    converted = int(weight) * 0.45
    print(f'you are {converted} kilos')
elif unit.upper() == "L":
    converted = int(weight) / 0.45
    print(f'you are {converted} pounds')
else:
    print("incorrect input")
    print("please enter either k or l")
