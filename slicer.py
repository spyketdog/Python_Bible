# Get the users email user name
email = input("What is your email address: ").strip()

# Slice out user name
user = email[ :email.index("@")]

# Slice domain name
domain = email[email.index("@") + 1:]

# Format message
output = "Your username is {} and your email is at {}".format(user,domain)
print(output)
