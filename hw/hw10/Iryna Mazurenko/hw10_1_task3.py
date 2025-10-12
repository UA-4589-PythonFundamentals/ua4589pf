from colorama import Fore, Style, init

# Initialize colors for Windows
init(autoreset=True)


class Employee:
    """
    Employee class stores information about an employee:
    - name
    - salary
    It also counts the total number of created objects.
    """

    count = 0  # Counter for the number of employees

    def __init__(self, name, salary):
        """Initialize the employee's name and salary and increase the counter."""
        self.name = name
        self.salary = salary
        Employee.count += 1

    def display_info(self):
        """Return formatted employee information with color highlighting."""
        return f"{Fore.CYAN}Employee Name:{Style.RESET_ALL} {self.name}, " \
               f"{Fore.YELLOW}Salary:{Style.RESET_ALL} {self.salary}"

    @classmethod
    def total_employees(cls):
        """Return the total number of created Employee objects."""
        return f"{Fore.GREEN}Total number of employees:{Style.RESET_ALL} {cls.count}"


# --- Main program ---
employees = []
n = int(input(f"{Fore.LIGHTBLUE_EX}Enter number of employees to add: {Style.RESET_ALL}"))

for i in range(n):
    name = input(f"{Fore.LIGHTBLUE_EX}Enter name of employee #{i + 1}: {Style.RESET_ALL}")
    salary = float(input(f"{Fore.LIGHTYELLOW_EX}Enter salary of {name}: {Style.RESET_ALL}"))
    employees.append(Employee(name, salary))

# --- Output ---
print(f"\n{Fore.LIGHTMAGENTA_EX}--- Employees ---{Style.RESET_ALL}")
for emp in employees:
    print(emp.display_info())

print(f"\n{Fore.LIGHTGREEN_EX}--- Total ---{Style.RESET_ALL}")
print(Employee.total_employees())

print(f"\n{Fore.LIGHTRED_EX}--- Class Information ---{Style.RESET_ALL}")
print(f"{Fore.YELLOW}Base class:{Style.RESET_ALL}", Employee.__base__)

print(f"\n{Fore.YELLOW}Namespace:{Style.RESET_ALL}")
for key in Employee.__dict__.keys():
    print(f" - {key}")

print(f"\n{Fore.YELLOW}Class name:{Style.RESET_ALL}", Employee.__name__)
print(f"{Fore.YELLOW}Module name:{Style.RESET_ALL}", Employee.__module__)
print(f"{Fore.YELLOW}Documentation:{Style.RESET_ALL}", Employee.__doc__)

