class A:

    def some_function(self):
        print('First function')

    def other_function(self):
        print("Second function")


class B:

    def method_in_B(self):
        print("Third function")


class C(A):

    def other_function(self):
        print("Replaced function")


class D(B, C):

    pass


# Let's see all the non-utility class attributes
print("A:\t", list(filter(lambda x: "__" not in x, dir(A))))
print("B:\t", list(filter(lambda x: "__" not in x, dir(B))))
print("C(A)\t", list(filter(lambda x: "__" not in x, dir(C))))
print("D(B,C)\t", list(filter(lambda x: "__" not in x, dir(D))))
print()

# Let's look at the implementation of functions in D
d = D()
d.method_in_B()
d.some_function()
d.other_function()
print()
