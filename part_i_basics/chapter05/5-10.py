current_users = ["peTer", "jesSe", "waLter", "adMin", "Meg"]
new_users = ["Peter", "MeG", "chris", "lois", "brian"]
# current_users_lowercase = []
# for username in current_users:
#     current_users_lowercase.append(username.lower())
current_users_lowercase = [username.lower() for username in current_users]

for username in new_users:
    if username.lower() in current_users_lowercase:
        print(f"{username.title()} please enter new username!")
    else:
        print(f"{username.title()}, you registered succesfully!")