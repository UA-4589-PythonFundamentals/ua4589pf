# # print("Hello, World!"
# print("Hello, World!")
# def greet():
#     print("Hello, World!")
#     print("Welcome to Lesson 11."
#     print("Let's learn Python together!")

# greet()



# a = 10
# b = 10
# c = a / b
# print(c)

# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     c = a / b
#     print(c)
# except Exception as err:
#     print("Error:", type(err).__name__, err)


# print("Program continues...")


# try:
#     a = int(input("Enter your number: ")) # throws ValueError if input is not an integer

#     if a < 4:
#         b = a/(a-3) # throws ZeroDivisionError for a = 3
#     if a >= 4:
#         print("Value of b = ", b) # throws NameError
#     # note that braces () are necessary here for multiple exceptions
# # except (ZeroDivisionError, NameError, ValueError) as err:
# #     print("Error Occurred and Handled", type(err).__name__, err)
# except ZeroDivisionError as err:
#     print("1", type(err).__name__, err)
# except ArithmeticError as err:
#     print("Error Occurred and Handled", type(err).__name__, err)
# except NameError as err:
#     print("2", type(err).__name__, err)
# except ValueError as err:
#     print("3", type(err).__name__, err)
# # except:
# #     print("Some other error occurred")


# try:
#     a = int(input("Enter your number: ")) # throws ValueError if input is not an integer

#     if a < 4:
#         b = a/(a-3) # throws ZeroDivisionError for a = 3
#     if a >= 4:
#         print("Value of b = ", b) # throws NameError
# except ZeroDivisionError as err:
#     print("1", type(err).__name__, err)
# except ArithmeticError as err:
#     print("Error Occurred and Handled", type(err).__name__, err)
# except NameError as err:
#     print("2", type(err).__name__, err)
# except ValueError as err:
#     print("3", type(err).__name__, err)
# # except:
# #     print("Some other error occurred")


# try:
#     status_code = int(input("Enter status code: "))
# except ValueError as err:
#     print("Invalid input. Please enter a valid integer.", err)
# else:
#     if status_code == 200:
#         print("OK")
#     elif status_code == 404:
#         print("Not Found")
#     elif status_code == 500:
#         print("Internal Server Error")
#     else:
#         print("Unknown Status Code")
# finally:
#     print("Execution completed.")

# # print("Program continues...")
# def divide_numbers(a, b):
#     try:
#         result = a / b
#     except ZeroDivisionError as err:
#         print("Error: Division by zero is not allowed.")
#         return 0
#     except TypeError as err:
#         print("Error: Invalid input type. Please provide numbers.")
#         return -1
#     else:
#         return result
#     finally:
#         print("Execution of divide_numbers is complete.")
#         # return 99

# print(divide_numbers(10, 2))  # Should print 5.0
# print(divide_numbers(10, 0))  # Should handle division by zero
# print(divide_numbers(10, 'a'))  # Should handle invalid input type
# print("Program continues...")

# def read_file(file_path):
#     if not isinstance(file_path, str):
#         raise TypeError("File path must be a string.")
#     elif not file_path.endswith('.txt'):
#         raise ValueError("File must be a .txt file.")
#         # raise 10

# for i in ["document.txt", 123, "document.pdf"]:
#     try:
#         read_file(i)
#         print(f"{i}: File read successfully.")
#     except (TypeError, ValueError) as err:
#         print(f"{i}: Error - {type(err).__name__}: {err}")

class CustomError(Exception):
    """Custom exception class for demonstration."""

def check_positive(number):
    if number < 0:
        raise CustomError("Negative value provided.")
    else:
        print("Positive value:", number)

try:
    check_positive(-5)
except CustomError as err:
    print("CustomError occurred:", err)
