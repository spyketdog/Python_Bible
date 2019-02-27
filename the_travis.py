known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]

print(len(known_users))

while True:
    print("HI I are TrAvis.... ")
    name = input("What Are yOur NaMe....??? ").strip().capitalize()
    if name in known_users:
        print("NaMe eStaBliShed.....PlEase enTer " + name.swapcase())
        remove = input("Would you like to be removed.....??? ".swapcase() + "Y/N??")

        if remove == "y":
            known_users.remove(name)
            print("Cheers..." + name)
        if remove == "n":
            print("Enjou your stay... ".swapcase() + name)
        break
    else:
        print("Be gone intruder...!!!!!!".upper())
