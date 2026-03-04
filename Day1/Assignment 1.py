#2)Prime in Range
# start=int(input('Enter start no :'))
# end=int(input('Enter end no :'))
# num=start
#
# for num in range (start , end+1):
#     is_prime=True
#     if num>1:
#         for i in range (2,num):
#             if num%i==0:
#                 is_prime=False
#                 break
#         if is_prime == True :
#             print(num)


#1)Factorial
# num=int(input('Enter no :'))
# fact=1
# for i in range(num,1,-1):
#     fact=fact*i
# print(fact)


#3)swap
# num=int(input('Enter no :'))
# a=num//100
# b=(num%100)//10
# c=num%10
# num=c*100+b*10+a
# print(num)


#4)Count digits
# num=int(input('Enter no :'))
# count=0
# sum=0
# even=0
# odd=0
#
# temp=num
# while temp>0:
#     digit=temp%10
#
#     count+=1
#     sum=sum+digit
#     if digit%2==0:
#         even+=1
#     else:
#         odd+=1
#     temp=temp//10
#
# print(count)
# print(sum)
# print(even)
# print(odd)


#5) LCM & GCD
a=int(input('Enter no a :'))
b=int(input('Enter no b :'))
mn=min(a,b)

for i in range(1,mn+1):
    if a%i==0 and b%i==0:
        gcd = i
print("gcd:",gcd)

mx=max(a,b)
while True:
    if mx%a==0 and mx%b==0:
        break
    mx+=1
print('LCM:',mx)
