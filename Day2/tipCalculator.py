
print("Welcome to thetip calculator.")
totalBill = float(input("What was the total bill? $"))
percentageTip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
numOfPeople = int(input("How many people to split the bill? "))

amountPerPerson = (totalBill * (percentageTip/100) + totalBill) / numOfPeople

print(f"Each person should pay: {round(amountPerPerson,2)}")