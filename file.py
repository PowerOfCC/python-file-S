## We needed form the user
#Total Rent 
#Total food Ordred for Snackimg
#Ecectricity units spend
#Persons Living in flat/room
#Charge per unit

rent = int(input("Enter your Flat/Room Rent : "))
food = int(input("Enter The amount of food ordred : "))
electricity_spend = int(input("Enter the total of electricity spend : "))
charge_per_unit = int(input("Enter The Charge per unit : "))
person = int(input("Enter the number of people'S living in Room : "))

total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill) // person
print("Each person will pay = ", output)