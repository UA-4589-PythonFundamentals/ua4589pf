def process_age_input(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age % 2 == 0:
        return "The age is even."
    else:
        return "The age is odd."

def main():
    try:
        age_input = input("Enter your age: ")
        age = int(age_input)
        result = process_age_input(age)
        print(result)
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
