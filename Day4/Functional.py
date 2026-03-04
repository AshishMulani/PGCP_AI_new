from functools import reduce

nums = [1,2,3,4,5,6,7,8,9]
squares = list(map(lambda n : n*n , nums))
print(squares)
even = list(filter(lambda n : n%2==0 , nums))
print(even)
prod = reduce(lambda n1,n2: n1*n2, nums)
print(prod)

books = [['Python Programming', 900],
         [ 'Java 8', 789],
         ['JavaScript', 500]]

books.sort()
print(books)
books.sort(key=lambda item: item[1])
print(books)
print(min(books,key=lambda item: item[1]))
print(max(books,key=lambda item: item[1]))

books_list = list(map(lambda item:[item[0].upper() ,item[1]],books))
print(books_list)

price_greater_than_800= list(filter(lambda item:item[1]>800, books))
print(price_greater_than_800)

colors_data = [{'Name': 'Red', 'Rating': 65},
               {'Name': 'Yellow', 'Rating': 45},
               {'Name': 'Blue', 'Rating': 80},
               {'Name': 'Orange', 'Rating': 90},
               {'Name': 'Black', 'Rating': 70}]

by_rating=sorted(colors_data, key=lambda item: item['Rating'])
print(by_rating)
by_rating.reverse()
print(by_rating)
least = min(colors_data, key=lambda item: item['Rating'])
print(least)
most = max(colors_data, key=lambda item: item['Rating'])
print(most)
more_than_70 = list(filter(lambda item: item['Rating'] >70,
                           colors_data))
print(more_than_70)