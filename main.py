# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ").lower()
add_pepperoni = input("Do you want pepperoni? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
pizzaPrice = 0
if size == "s":
    pizzaPrice += 15
elif size == "m":
    pizzaPrice += 20
elif size == "l":
    pizzaPrice += 25
else:
    print("Wrong value! please type S, M or L")

if add_pepperoni == "y":
    if size == "s":
        pizzaPrice += 2
    else:
        pizzaPrice += 3

if extra_cheese =="y":
    pizzaPrice += 1

print(f"Your final bill is ${pizzaPrice}")
       