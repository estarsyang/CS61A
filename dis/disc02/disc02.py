# 1.1 Draw the environment diagram that results from executing the code below.

def curry2(h):
    def f(x):
        def g(y):
            return h(x, y)
        return g
    return f
make_adder = curry2(lambda x, y: x + y)
add_three = make_adder(3)
add_four = make_adder(4)
five = add_three(2)



# 1.2 Write curry2 as a lambda function
curry2 = lambda h: lambda x: lambda y: h(x, y)

# 1.3 Draw the environment diagram that results from executing the code below.
n = 7
def f(x):
    n = 8
    return x + 1
def g(x):
    n = 9
    def h():
      return x + 1
    return h
def f(f, x):
    return f(x + n)

f = f(g, n)
g = (lambda y: y())(f) # 15

# 1.4
y = "y"
h = y
def y(y):
    h = "h"
    if y == h:
      return y + "i"
    y = lambda y: y(h)
    return lambda h: y(h)
y = y(y)(y) # hi