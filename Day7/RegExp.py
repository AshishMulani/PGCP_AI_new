import re

msg='good morning have a good day good bye'

# match=re.search(r'h',msg)
# if match:
#     print(match.span())
#     print(match.group())
#
# else:
#     print('no match')
#
#
# print(re.findall(r'good',msg))

words="sit bit pit mit it fat unit"

print(bool(re.search(r'^sit',words)))
print(bool(re.search(r"unit$",words))) #match is capable of finding at only start

print(re.findall(r'\b[a-z]*it\b',words))

pattern=r'\b[a-z]+it\b'
print(re.findall(pattern,words))

pattern=r'\b[a-z]?it\b'
print(re.findall(pattern,words))

pattern=r'\b[a-z]{1}it\b'
print(re.findall(pattern,words))

pattern=r'\b\w{1}it\b'
print(re.findall(pattern,words))

rules='a b Z T Y 0 5 6 7 ^*&^%*%      '


