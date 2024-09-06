pizzas = ["margherita", "pepperoni", "vegetarian", "prosciutto"]

# for pizza in pizzas:
#     print(f"I like {pizza} pizza!")

print("First 3 items of the list are:")
for pizza in pizzas[0:3]:
    print(pizza)

print("2 middle items of the list are:")
for pizza in pizzas[1:3]:
    print(pizza)

print("Last 3 items of the list are:")
for pizza in pizzas[-3:]:
    print(pizza)