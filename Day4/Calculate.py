import Math

# from Math import add //avoid
# from Math import sub as s
# import Math as m

operation=int(input('enter the operation you want to perform:\n add=1,sub=2,multiply=3,division=4'))
num1=int(input('Enter the number 1:'))
num2=int(input('Enter the number 2:'))

if operation==1:
    result= Math.add(num1, num2)
    # result = add(num1, num2)
    print(result)

elif operation==2:
    result = Math.sub(num1, num2)
    # result = m.sub(num1, num2)
    # result = s(num1, num2)
    print(result)

elif operation==3:
    result = Math.mult(num1, num2)
    print(result)

elif operation==4:
    result = Math.div(num1, num2)
    print(result)

else:
    print('Wrong choice')