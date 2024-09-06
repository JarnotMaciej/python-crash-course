pizzas = ["margherita", "pepperoni", "vegetarian", "prosciutto"]
friend_pizzas = pizzas[:]
pizzas.append("funghi")
friend_pizzas.append("supreme")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friends favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)