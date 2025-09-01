print(__name__)
def print_l2_info():
    print("level 2")
    print(f"Module name: {__name__}")
    print(f"Module file: {__file__}")
    # print(f"Module path: {__path__}")


if __name__ == "__main__":
    print_l2_info()