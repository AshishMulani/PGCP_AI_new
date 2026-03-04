# Q1. Define a function overlapping () that takes two lists and returns True if they have at
# least one member in common, False otherwise.

# def overlapping(l1,l2):
#     flag=False
#     for i in l1:
#         for j in l2:
#             if i==j:
#                 flag=True
#     return flag
#
# l1=[1,2,3,4,5]
# l2=[7,9,6,7,8]
# print(overlapping(l1,l2))


# Q.2.In English, present participle is formed by adding suffix -ing to infinite form: go -> going. A simple set of rules can be given as follows:
#  a. If the verb ends in e, drop the e and add ing
#  b. If the verb ends in ie, change ie to y and add ing
# Write a function make_ing_form() which accepts a list of verbs and returns a dictionary with verb : present participle

# words=list(input('enter the verbs:'))
# verbs=['make','die','play']
# print(verbs)
#
# def make_ing_form(*verbs):
#     new_list = []
#     for v in verbs:
#         if v.endswith('ie'):
#             word = v[:-2]+'ying'
#
#         elif  v.endswith('e'):
#             word=v[:-1]+'ing'
#
#         else:
#             word=v+'ing'
#
#         new_list.append(word)
#     return new_list
#
# print(make_ing_form(*verbs))






# Q.3. Function display_greeting(message) prints message sent as argument as today's greeting. Decorate the function using appropriate decorated so that the greeting is displayed using Uppercase.
# def upper(inner):
#     def wrapper(message):
#         message=message.upper()
#         return inner(message)
#     return wrapper
#
# @upper
# def display_greeting(message):
#     print(message)
#
# display_greeting('Good Morning')

# Q. 4. Create series of 'n' prime numbers and display first 10



# Q.5
emp_data = {'Amol': ['C', 'C++', 'Java'], 'Aditya': ['Angular', 'Java'],
           'Aditi': ['Python', 'PHP', 'Database']}

# 1. Find employees that know 'python'
l1=dict(filter(lambda item:'Python'in item[1],emp_data.items()))
print(l1)

# 2. Add a new skill - 'test' in skillset of all employees

# 3. Sort employees by skills
# for the given dictionary of employees

# Q.6
# Following data displays min/max/average temp for cities
# weather= [{'Mumbai' : [28, 30, 32]},.....]
#
# 1. Print the weather data
# 2. Print the city with maximum/min temp
# 3. Print all the cities that expereince min temp more than 30 degree
# 4. Create a dictionary to print 'City':'Ave temp'