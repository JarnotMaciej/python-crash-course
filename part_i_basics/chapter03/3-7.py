guests = ["lucas", "sophia", "noah", "amelia", "elijah"]
guests.insert(0, "nathan")
guests.insert(2, "jessica")
guests.append("olivier")

print("I can invite only 2 people for dinner!")
guests.pop()
guests.pop()
guests.pop()
guests.pop()
guests.pop()
guests.pop()

print(f"Dear, {guests[0].title()}! I invite you for dinner!")
print(f"Dear, {guests[1].title()}! I invite you for dinner!")

# print(guests)
del(guests[1])
del(guests[0])
print(guests)
