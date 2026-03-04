my_str='python is dynamic language'
# print('Python' in my_str)
# print('Java' not in my_str)
#
# for ch in my_str:
#     print(ch)
# print('-------------------------------------------------------------')
# #Indexing and Slicing
# print(my_str[3])
# print(my_str[-3])
# print(my_str[4:10])
# print(my_str[-14:-10])
# print(my_str[4:20:2])
# print(my_str[20:4:-2])
# print(my_str[4:20:-2])
# print(my_str[::-1])
# print(my_str[:4]+ my_str[4:])
# print(my_str[-14:-10:2])

print('-------------------------------------------------------------')
#character classification
# value='abc'
# print(value.isalpha())
# value='123'
# print(value.isdecimal())
# value='123\u00B2'
# print(value.isdigit())
# value='123\u00B2\u2168'
# print(value.isnumeric())
# print(value.isdigit())
# value='abc12.3\u00B2\u2168'
# print(value.isalnum())
# print(my_str.isalnum()) #space is not allowed

print('-------------------------------------------------------------')
#Case Conversion
# print(my_str.upper())
# print(my_str.lower())
# print(my_str.capitalize())
# print(my_str.title())
# print(my_str.swapcase())
# print('-------------------------------------------------------------')
# my_str='python is a dynamic language'
# #Other Methods
# print(my_str.startswith('Python'))
# print(my_str.endswith('Python'))
# print(my_str.find('a'))
# print(my_str.rfind('a'))
# print(my_str.count('a'))
# print(my_str.index('l'))
# print(my_str.replace('a', 'e',1))
#
# words=my_str.split(' ')
# print(words)
#
# sentences=' '.join(words)
# print(sentences)
#
# sentences='#'.join(words)
# print(sentences)
#
# parts=my_str.partition('is')
# print(parts)
#
# parts=my_str.partition('fff')
# print(parts)
#
# parts=my_str.partition('.')
# print(parts)

print('hello', end="\t")
print('world')

print(ord('A'))
print(chr(97))

my_str1="          hello          "
my_str1=my_str1.strip()
print(my_str1)