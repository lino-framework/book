""" generator functions

>>> print(f1())
[0, 1, ..., 999]

>>> print(f2())
<generator object f2 at ...>

"""


def f1():
    l = []
    for i in range(1000):
        l.append(i)
    return l

def f2():
    for i in range(1000):
        yield i  # yield ulatama

# for i in f1():
#     print i

# # to iterate =
# for i in f2():
#     print i

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
