import uuid

class User:
    def __init__(self, name, age, email, password):
        self.id = uuid.uuid4()
        self.name = name
        self.age = age
        self.email = email
        self.password = password

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, age={self.age}, email={self.email}, password={self.password})"
    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "age": self.age,
            "email": self.email,
            # Note: Password is intentionally excluded for security reasons
        }
    
def generate_random_users(count=10):

    return [User(name=f"User {i}", age=20 + i, email=f"user{i}@example.com", password=str(uuid.uuid4())) for i in range(count)]

if __name__ == "__main__":
    users = generate_random_users(5)
    for user in users:
        print(user)
        print(user)
        print(user.to_dict())

