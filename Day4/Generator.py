def generate_series():
    i =0
    while True:
        yield i
        i+=1
series = generate_series()
print(next(series))
print(next(series))
print(next(series))
print(next(series))

def fib_generator(n):
    i = 0
    a,b = 0, 1
    while i < n:
        yield b
        a,b = b, a+b
        i+=1

fib_numbers = fib_generator(10)
for j in range(10):
    print(next(fib_numbers))