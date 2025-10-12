def process_age(age):
    """Process entered age and return whether it's even or odd."""
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age % 2 == 0:
        return "even"
    else:
        return "odd"


def main():
    try:
        user_input = input("Enter your age: ")
        age = int(user_input)
        result = process_age(age)
        print(f"Your age is {result}.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception:
        print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
