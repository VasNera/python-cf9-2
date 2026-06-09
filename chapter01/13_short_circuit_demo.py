name = 'Bob'

print("****** or *****")
valid_user = None or "User"

print(valid_user)


print("****** and *****")
email = "bob@aueb.gr"

valid_email = email and True
print(f"valid_email: (valid_email)")

valid_email = email and "give your email"
print(f"valid email: {valid_email}" )
