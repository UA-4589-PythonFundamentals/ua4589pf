import validator as v

def password_typing():
    
    while True:
        try:
            password = input("Enter password: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n! Input interrupted. Exiting program.")
            break

        errors = v.check_password(password)

        if errors:
            print("Password is invalid:")
            for err in errors:
                print("   ", err)
            print("Try again.\n")
        else:
            print("✅ Password is valid!")
            break


if __name__ == "__main__":
    password_typing()