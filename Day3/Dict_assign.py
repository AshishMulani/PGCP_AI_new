# def cipher(ch)
#
#     {ch:cipher(ch) for ch in }
#
#     askii lower case
#
# #Q1
letters=['a','b','c','d','e','f','g','h','i','j','k',
         'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
shift=int(input('enter the shift value:'))
# cipher={}
cipher={letters[i]:letters[(i+shift)%len(letters)] for i in range(len(letters))}
print(cipher)

original=input('enter the encrypted word:')
decrypted={key:value for key,value in cipher.items()}
# 3

# print('Decrypted dictionary :',decrypted)

def cipher(items):
    result = ''
    for ch in items:
        for key,value in decrypted.items():
            if ch==value:
                result+=key
    return result
print(cipher(original))



#Q2
# emp_data={'Amol':['c','c++','java'],
#           'Aditya':['angular','java'],
#           'Aditi':['python','php','database']}
# #1
# for key, value in emp_data.items():
#     print(f'{key}-{value}')
#
# #2
# if emp_data.item()=='java':
#     print(emp_data.item())
#
# #3
# name=input('enter the name of emp:')
# if emp_data.item
# emp_data.update({name})

