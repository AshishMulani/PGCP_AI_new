#if-else
age=int(input("Enter age:"))
if age>18:
    print('Permitted')
else :
    print('Not permitted')

#Nested if-else
gender=input('Enter gender M/F :')
if age>18:
    if gender == 'M':
        print('Man')
    else:
        print('Woman')
else :
    print('Child')


#elif
if age>18 and gender=='M':
    print('MAN')
elif age>18 and gender=='F':
    print('Woman')
else:
    print('Child')


marks=int(input('Enter Marks:'))
if 85<marks<100:
    print('A')
if 60<marks<85:
    print('B')
if 45<marks<60:
    print('C')
else:
    print('D')