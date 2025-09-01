print(__name__)
# __all__ = ["print_l1_info", "__a"]

def print_l1_info():
    print("level 1")
    print(f"Module name: {__name__}")
    print(f"Module file: {__file__}")
    # print(f"Module path: {__path__}")


a = 1
_a = 2
__a = 3

if __name__ == "__main__":
    print_l1_info()