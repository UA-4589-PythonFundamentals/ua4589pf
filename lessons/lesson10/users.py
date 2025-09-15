class User:
    count = 0

    def __init__(self, username, email):
        self.pk = self.get_total_users()
        self.username = username
        self.email = email
        User.count += 1

    def display_info(self):
        return f"ID: {self.pk}, Username: {self.username}, Email: {self.email}"

    @classmethod
    def get_total_users(cls):
        print(f"Class method called from {cls}")
        return cls.count
    
    # @staticmethod
    # def is_valid_email(email):
    #     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    #     return re.match(pattern, email) is not None
    
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

users = [User("Alice", "alice@example.com"), User("Bob", "bob@example.com")]
print(users[0].display_info())
print(users[1].display_info())
print("Total users:", User.count)
# print(User.display_info()) # This will raise an error because display_info requires an instance
print(User.display_info(users[0]))  # This works but is not a common practice

print(User.get_total_users())  # Correct way to call class method
print(users[0].get_total_users())  # This also works but is less common