nums=[1,2,3,4,5,6,7,8,9]
squares=[]
for num in nums:
    squares.append(num*num)
    print(squares)

squares=[num*num for num in nums]
print(squares)
sq_even=[num*num for num in nums if num%2==0]
print(sq_even)

even_odd=['even' if num%2==0 else 'odd'
          for num in nums]
print(even_odd)

prices=[1000,780,980,560,450,460]
def calculate_discount(p):
    return p*0.8
discounted=[calculate_discount(p) for p in prices]
print(discounted)

books=[[123, 'Python Programming', 900], [3445,'Java', 789], [566, 'JS', 500]]
discounted=[calculate_discount(item[2]) for item in books]
print(discounted)

my_str="Was it a rat I saw?"
cleaned=[ch.lower() for ch in my_str if ch.isalpha()]
print(''.join(cleaned))
if cleaned==cleaned[::-1]:
    print('Palindrome')
else:
    print('Not a palindrome')