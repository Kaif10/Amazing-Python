#func prac

def cost(qty, item, price):
    print(f'{qty} {item} cost ${price:.2f}')

cost('bananas', 1.74, 6)
# Output: bananas 1.74 cost $6.00


def avg(a):
   total = 0
   for v in a:
      total += v
   return total / len(a)


print(avg([1, 2, 3, 4, 5]))
#3.0

t = (1, 2, 3, 4, 5)
print(avg(t))
#3.0



#Think of *args as a variable-length positional argument list,
# and **kwargs as a variable-length keyword argument list.

def avg_2(*args):
   return sum(args) / len(args)


print(avg_2(1, 2, 8, 4, 5))
#4.0


def keyword_func(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, val in kwargs.items():
             print(key, '->', val)


keyword_func(foo=1, bar=2, baz=3)



def fun_both(a, b, *args, **kwargs):
   print(F'a = {a}')
   print(F'b = {b}')
   print(F'args = {args}')
   print(F'kwargs = {kwargs}')


fun_both(1, 2, 'foo', 'bar', 'baz', 'qux', x=100, y=200, z=300)
#a = 1
#b = 2
#args = ('foo', 'bar', 'baz', 'qux')
#kwargs = {'x': 100, 'y': 200, 'z': 300}



