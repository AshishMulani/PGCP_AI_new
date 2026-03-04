# Q1. Define a function overlapping () that takes two lists and returns True if they have at
# least one member in common, False otherwise.

def overlapping(l1,l2):
    flag=False
    for i in l1:
        for j in l2:
            if i==j:
                flag=True
    return flag

l1=[1,2,3,4,5]
l2=[7,9,6,7,8]
print(overlapping(l1,l2))


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
n=int(input('Enter series size : '))
series=[i for i in range(1,n+1)]
print(series)

prime=list(filter(lambda v:v>1 and all( v%j!=0 for j in range(2,v)),series))
print(prime[:10])


# Q.5
# emp_data = {'Amol': ['C', 'C++', 'Java'], 'Aditya': ['Angular', 'Java'],
#            'Aditi': ['Python', 'PHP', 'Database']}
#
# # 1. Find employees that know 'python'
# l1=dict(filter(lambda item:'python'in [i.lower() for i in item[1]],emp_data.items()))
# print(l1)

# # 2. Add a new skill - 'test' in skillset of all employees
# l2=dict(map(lambda item:(item[0], item[1]+['test']),emp_data.items()))
# print(l2)
# #or
# l2={k:(lambda v:v+['test'])(v) for k,v in emp_data.items()}
# print(l2)

# 3. Sort employees by skills
# l3=dict(sorted(emp_data.items(),key=lambda item:item[1]))
# print(l3)


# # Q.6
# # Following data displays min/max/average temp for cities
# weather= [{'Mumbai' : [28, 30, 32]},
#           {'Pune':[34,35,26]},
#           {'Nashik': [24, 25, 27]}]
# #
# # 1. Print the weather data
# print(weather)
#
# # 2. Print the city with maximum/min temp
# print(max(weather,key=lambda item: max(list(item.values())[0])))
# print(min(weather,key=lambda item: min(list(item.values())[0])))
#
# # 3. Print all the cities that expereince min temp more than 30 degree
# print(list(filter(lambda item: any(item>30 for item in list(item.values())[0]),weather)))
#
# # 4. Create a dictionary to print 'City':'Ave temp'
# avg_temp=dict(map(lambda v: (list(v.keys())[0],sum(list(v.values())[0])/len(list(v.values())[0])),weather))
# print(avg_temp)