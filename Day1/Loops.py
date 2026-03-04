#Loops
for i in range(10):
    print(i)
print('-----------------------------------')
for i in range(1,11,3):
    print(i)
print('-----------------------------------')
for i in range(67, 33, -4):
    print(i)
print('-----------------------------------')

#break
for i in range(10):
    if i==6:
        break
    print(i)

#continue
for i in range(10):
    if i==6:
        continue
    print(i)

#prime numbers
flag=True
num=int(input("Enter no:"))
for i in range(2,num):
 if num%i==0:
    flag=False
    break
if flag:
    print('Prime')
else:
    print('Non Prime')
print('-----------------------------------')

for i in range (2,num):
    if num%i==0:
        print('Non Prime')
        break
else:
    print('Prime')
print('-----------------------------------')

# while loop
i=0
while i<10:
    print(i)
    i+=1
print('-----------------------------------')

i=0
while i<10:
  i+=1
  if i==6:
    continue
  print(i)
print('-----------------------------------')

while i<10:
    if i==6:
        continue
    print(i)
i+=1

