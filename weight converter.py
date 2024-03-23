Choice = input(print("Type number 1 for kg to lbs. Type number 2 for lbs to kg: "))
Weight = float(input("Insert the weight you want to calculate: "))

if Choice == "1":
    print(Weight * 2.2)
elif Choice == "2":
    print(Weight / 2.2)
else:
    print("Invalid choice")