class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f'{self.name} <{self.email}>'


class NewUser:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __hash__(self):
        return hash(self.email)

    def __eq__(self, obj):
        return self.email == obj.email


user_1 = User('Anna Williams', 'annawilliams@example.com')
print(user_1)
print()
user_2 = NewUser('Anna Williams', 'annawilliams@example.com')
user_3 = NewUser('Anna Collins', 'annawilliams@example.com')
print(f"'{user_2.name}' and '{user_3.name}' are the same user:", user_2 == user_3)
print("The hash of users are:")
print(hash(user_2))
print(hash(user_3))
print(f"The set of unique user emails for '{user_2.name}' and '{user_3.name}' is: ",
      {user: user.email for user in [user_2, user_3]})
