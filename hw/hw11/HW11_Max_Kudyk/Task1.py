def process_age(age):
  if age < 0:
    raise ValueError("Error: Age cannot be a negative number")

  if age % 2 == 0:
    print(f"Your age, {age}, is an even number")
  else:
    print(f"Your age, {age}, is an odd number")


if __name__ == "__main__":
  try:
    user_age = int(input("Please, enter your age: "))
    process_age(user_age)
  except ValueError as e:
    print(e)