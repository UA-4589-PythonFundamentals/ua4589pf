from mylog import logging

class UserException(Exception):
    """Custom exception for user-related errors."""
    def __init__(self, message):
        super().__init__(message)
        logging.error(f"UserException occurred: {message}")
    pass


class UserModel:
    def __init__(self, username, email, age=10):

        try:
            self.age = int(age)
        except (TypeError, ValueError):
            raise UserException("Age must be an integer or None.")
        if not isinstance(username, str) or not isinstance(email, str):
            raise UserException("Username and email must be strings.")
        if "@" not in email:
            raise UserException("Invalid email address.")
        self.username = username
        self.email = email
        logging.info(f"UserModel created for {self.username}")

    def __repr__(self):
        return f"UserModel(username={self.username}, email={self.email})"
    

if __name__ == "__main__":
    user = UserModel("john_doe", "john@example.com")
    print(user)
    try:
        user_invalid = UserModel("jane_doe", "janeexample.com")  # This will raise UserException
    except UserException as err:
        print("Error occurred:", err)
    else:
        print(user_invalid)
    try:
        user_invalid = UserModel("jane_doe", "jane@example.com", "test")  # This will raise UserException
    except UserException as err:
        print("Error occurred:", err)
    else:
        print(user_invalid)