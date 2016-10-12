# generator functions


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

print f1()
print f2()

