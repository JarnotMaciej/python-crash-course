usernames = ["peter", "jesse", "walter", "admin", "meg"]

for username in usernames:
    if (username == "admin"):
        print(f"Hello {username}, here is your admin panel...")
    elif (username == "meg"):
        print(f"Shut up {username}!")
    else:
        print(f"Hello {username}, how are you?")