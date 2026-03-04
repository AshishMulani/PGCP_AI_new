def simple_function():
    print('hello')

simple_function()

def add(n1:int,n2:int):
    return n1+n2

print(add(8,9))
print(add('hello', 'world'))
print(add(89.7, 7.9))

def calculate_discount(product='book', price=1000):
    price = price *0.8
    print(f'Price of {product} after discount :{price}')

calculate_discount('book', 900)
# calculate_discount(900, 'book')
calculate_discount(price=900, product='book')
calculate_discount()
calculate_discount('pen')
calculate_discount(price=700)

def addition(*nums):
    total =0
    for num in nums:
        total +=num
    return total

numbers = [1,2,3,4,5,6,7]
print(addition(12,3,7,8,8,9,10))
print(addition(*numbers))

def calculate_ave_marks(**kwargs):
    name = kwargs['name']
    marks = kwargs['marks']
    total =0
    for mark in marks:
        total += mark
    print(f'Average marks obtained by {name} : {total/len(marks)}')

calculate_ave_marks(name='abc', marks=[87,78, 90], dept='Comp')
student_data ={'name':'xyz',
               'marks' : [90,77,80]}
calculate_ave_marks(**student_data)