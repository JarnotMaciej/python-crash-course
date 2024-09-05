weird_name = "    \n\t J o H \n n \t\t   "

print(weird_name)
print(weird_name.lstrip())
print(weird_name.rstrip())
print(weird_name.strip())
print(weird_name.strip().replace(" ", "").replace("\n", "").title())