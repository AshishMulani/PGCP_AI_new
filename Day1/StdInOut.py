name=input('Enter name:')
age=int(input('Enter age:'))
print('You have entered', name , 'and' , age) #simple
print('You have entered {} and {}'.format(name, age)) #format function
print(f'You have entered {name} and {age}') #format strings

#Numbers
no=4e6
print(no)
print(f'{no:.0f}')
print(f'{no:.2f}')
print(f'{no:,.0f}')

#Spacing and Padding
num=25
print(num)
print(f'{num:<10}')
print(f'{num:>10}')
print(f'{num:^10}')
print(f'{num:10}')
print(f'{num:08}')

#for %
marks=0.75
print(f'{marks:0%}')
print(f'{marks:.0%}')
print(f'{marks:.2%}')




