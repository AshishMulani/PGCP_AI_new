fruits=['mango', 'banana', 'watermelon', 'guava', 'orange']
print(fruits)
fruits1= {'mango', 'banana', 'watermelon', 'guava', 'strawberry', 'grapes'}

# for fruit in fruits:
#     print(fruit)
# print('mango' in fruits)
# print('pomegranate' not in fruits)
# fruits.add('pomegranate')
# print(fruits)
# fruits.remove('banana')
# print(fruits)
# fruits.discard('banana')
# print(fruits)
# # fruits.remove('banana')
# # print(fruits)
# fruits.pop()
# print(fruits)

u_fruits=fruits.union(fruits1)
print(u_fruits)
u_fruits=fruits | fruits1
print(u_fruits)
print('------------------------------------------------')
i_fruits=fruits.intersection(fruits1)
print(i_fruits)
i_fruits=fruits & fruits1
print(i_fruits)
print('------------------------------------------------')
d_fruits=fruits.difference(fruits1)
print(d_fruits)
d_fruits=fruits - fruits1
print(d_fruits)
print('------------------------------------------------')
s_fruits=fruits.symmetric_difference(fruits1)
print(s_fruits)
s_fruits=fruits ^ fruits1
print(s_fruits)



