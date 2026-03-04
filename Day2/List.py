words=['cat', 'bat', 'rat', 'sat','pat']
# for word in words:
#      print(word)
#
# print(len(words))
# print('cat' in words)
# print('mat' not in words)
#
# # print("-----------Indexing and Slicing--------------")
print(words[4])
print(words[-3])
# print(words[5])
print(words[2:4])
print(words[1:4:2])
print(words[4:1])
print(words[4:1:-1])
print(words[::-1])
print(words[:2] + words[2:])

#Methods


#isinstance
for word in words:
    if isinstance (word,list):
        for item in word:
            print(item)
    else:
        print(word)

#enumerate
for i,j in enumerate(words):
    print(i, ' ', j)


#unpacking
books=[[123, 'Python Programming', 900], [3445,'Java', 789], [566, 'JS', 500]]
for isbn, title, price in books:
    print(f'{isbn}-{title}-{price}')

#sorting
def get_len(item):
    return len(item)
cards=['heart','spade','diamond','club']
cards.sort(key=get_len)
print(cards)

min_len_cards=min(cards,key=get_len)
print(min_len_cards)






