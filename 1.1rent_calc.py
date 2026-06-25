house_rent = int(input("Enter amount of rent: "))
electricity_unit = int(input("Enter unit of electricity: "))
water_bill = int(input("Enter amount of water bill: "))
wifi = int(input("Enter amount of wifi: "))
person = int(input("Enter number of person in flat: "))
ele_price = int(input("Enter electricity price per unit: "))
total_electricity = electricity_unit*ele_price
Total_price = house_rent + total_electricity + water_bill + wifi 
print("Total expenses of a month is: ",Total_price)
ee = Total_price/person
print("Each person has to pay: ",ee)