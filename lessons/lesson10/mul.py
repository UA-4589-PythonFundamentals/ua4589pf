class A:
    def print_a(self):
        print("A")

class B:
    def print_b(self):
        print("B")

class C:
    def print_c(self):
        print("C")

class D(B, A):
    def print_d(self):
        print("D")
    def print_b(self):
        print("B from D")
    def old_print_b(self):
        super().print_b()
class E(C, A):
    def print_e(self):
        print("E")
    def print_b(self):
        print("B from E")
class F(D, E):
    def print_f(self):
        print("F")


f = F()

f.print_a()
f.print_b()
print(f.__dict__)
print(F.__dict__)
print(F.mro())

print("===")
print(A.__dict__)
print(B.__dict__)
print(C.__dict__)
print(D.__dict__)
print(E.__dict__)
print(F.__dict__)