def increment(num):
    return num+1

incre = increment
i = 10
print(incre(i))

def get_len(item):
    return len(item[0])

cards = ['heart', 'spade', 'diamond', 'club']
cards.sort(key=get_len)
print(cards)

"""lambda arg_list : <expression>"""

get_len = lambda item : len(item)

cards.sort(key=lambda item:len(item))
print(cards)

l1 = lambda n : n>100
print(l1(120))

l2 = lambda n1,n2 : n1+n2
print(l2(9,10))

l3 = lambda *args: sum(args)
print(l3(1,2,3,4,4))

l4 = lambda **kwargs:sum(kwargs.values())
print(l4(one=1, two=2, three=3))


