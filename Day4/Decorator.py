def outer(inner):
    def wrapper():
        inner()
    return wrapper

def smart_math(inner):
    def wrapper(*args):
        a, b = args
        if a <b:
            a,b = b,a
        return inner(a,b)
    return wrapper

@smart_math
def subtract(n1, n2):
    return n1-n2

print(subtract(3,10))
print(subtract(13,10))