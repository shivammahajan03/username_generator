# get user email address

email = input("Hi there, I'm your helpful username generator. \nPlease enter your email address - ").strip()

# Slice out user name

user_name = email[:email.index("@")]

# Slice domain name

domain = email[email.index("@") + 1:]

# Format message

output = """Your assigned username is '{}' and your domain name is '{}'. \nHappy Surfing!""".format(user_name, domain)

# display output message

print(output)


