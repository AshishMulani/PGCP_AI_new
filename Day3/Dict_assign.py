
# #Q1
# letters=[chr(i) for i in range(ord('a'),ord('z')+1)]
# print(letters)
# shift=int(input('enter the shift value:'))
#
# decrypted={letters[i]:letters[(i+shift)%len(letters)] for i in range(len(letters))}
# print(decrypted)
#
# original=input('enter the encrypted word:')
#
# def cipher(items):
#     result = ''
#     for ch in items:
#         for key,value in decrypted.items():
#             if ch==value:
#                 result+=key
#     return result
#
# print(cipher(original))



#Q2
emp_data={'Amol':['c','c++','java'],
          'Aditya':['angular','java'],
          'Aditi':['python','php','database']}

#1 Print employees and their skill sets
for key, value in emp_data.items():
    print(f'{key}-{value}')

#2 Find all the employees who know Java
for key, value in emp_data.items():
    if 'java' in value:
        print(key)

# #3 Update skill for an employee
# name=input('enter the name of emp:')
# for key, value in emp_data.items():
#     if name in key:
#         skills=input(f'enter skills of {key}:')
#         skill_list=skills.split(',')
#         emp_data.update({key:skill_list})
#
# for key, value in emp_data.items():
#     print(f'{key}-{value}')


#4 Add/remove employee data
emp_data['Ashish']=['python','ML','DL']
for key, value in emp_data.items():
    print(f'{key}-{value}')

emp_data.pop('Ashish')
for key, value in emp_data.items():
    print(f'{key}-{value}')