# #Que 1
# num=int(input("Enter the no of words :"))
# count=0
# # input("Enter the words :")
# words=[]
# length=0
#
# for i in range(1,num+1):
#     word=input(f"Enter the {i} word :")
#     if length<len(word):
#         length=len(word)
#         new_w=word
#
#     words.append(word)
# print(words)
#
# print(f'the longest word is \'{new_w}\' with length {length}')


# #Q2 Remove duplicates
# num=int(input("Enter the no of words :"))
# words=[]
# for i in range(1,num+1):
#     word=input(f"Enter the {i} word :")
#     words.append(word)
# print(words)
#
# u_words = []
# for word in words:
#     if word not in u_words:
#         u_words.append(word)
#
# print("List after removing duplicates:", u_words)
#

#
# #Q3
# booklist=[]
# num=int(input('No of books you want to add:'))
#
# for i in range(num):
#     name=input('book name:')
#     price =int(input('Price:'))
#     booklist.append([name,price])

# booklist=[['java 8',700],['python for programming',500], ['C++', 555]]
# print(booklist)
# 1
# booklist.append(['C++',400])
# print(booklist)

#2
# for book in booklist :
#     if book[0]=='C++':
#         booklist.remove(book)
#         break
# print("After removing:", booklist)


#3
# for book in booklist:
#     if book[0]=='java 8':
#         book[1]=788
#         break
# print("After updating price :",booklist)

#4
# def sort_name(book):
#     return book[0]
# booklist.sort(key=sort_name)
# print('after sorting by name',booklist)
#
# #5
# def sort_price(book):
#     return book[1]
# booklist.sort(key=sort_price)
# print('after sorting by price',booklist)

#6
# def price(book):
#     return book[1]
# max_book=max(booklist,key=price)
# min_book=min(booklist,key=price)
# print('Max price book:',max_book)
# print('Min price book:',min_book)

# #Q4
# t1=(1, 2, 3, 4)
# t2=(3, 5, 2, 1)
# t3=(2, 2, 3, 1)
# print(t1,'\n',t2,'\n',t3)
# result=tuple(a+b+c for a,b,c in zip(t1,t2,t3))
# print(result)

#Q5
t1=tuple(input('enter the tuple elements:'))
print(t1)

repeat=[]
for i in range(len(t1)):
    for j in range(i+1,len(t1)):
        if t1[i]==t1[j]and t1[i] not in repeat:
            repeat.append(t1[i])
repeat=tuple(repeat)
print('repeated items:',repeat)