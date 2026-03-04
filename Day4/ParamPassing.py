def increment(no):
    no +=1

def increment_l(num):
    num[0] = num[0]+1


number = 10
increment(number)
print(number)
lst = [10]
increment_l(lst)
print(lst)