
def task1(a: int, b: int) -> int:
    """Return the largest number of two numbers"""
    return a if a > b else b

print(task1(4, -5))
print("___________")

task2_rectangle = lambda width, height: width * height
task2_triangle = lambda base, height: .5 * base * height
task2_circle = lambda radius: radius * radius * 3.14

print(task2_rectangle(2, 5))
print(task2_triangle(2, 5))
print(task2_circle(5))
print("___________")

def task3(input: str) -> dict:
    set_input = set(input)
    result = {}
    for el in set_input:
        if el in input:
            result.update({el: input.count(el)})
    
    return result

print(task3("hello"))