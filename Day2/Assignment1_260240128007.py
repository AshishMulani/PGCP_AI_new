'''Q.1A. Write a program that asks the user how many days are in a particular month, and
what day of the week the month begins on (0 for Monday, 1 for Tuesday, etc), and then
prints a calendar for that month. For example, here is the output for a 30-day month that begins on day 3 (Thursday):
M  T  W  T  F  S  S
         1  2  3  4
5  6  7  8  9 10 11 '''

days=int(input('Enter no of days:'))
start=int(input('enter the day where you want to start:'))

my_str="M\tT\tW\tT\tF\tS\tS"
print(my_str)
for i in range(start):
    print('\t',end='')

for i in range(1,days+1):
    print(i,end='\t')

    if (start+i)%7==0:
        print()




'''Q. 2. Check if all letters in a string are uppercase'''

my_str=input('enter the string:')
print(my_str)
is_upper=True
my_str=my_str.replace(' ','')
for ch in my_str:
    if not 'A'<=ch<='Z':
        is_upper = False

print(is_upper)


'''Q. 3. Write a version of a palindrome recognizer 
that also accepts phrase palindromes such as : Was it a rat I saw? or 
Dammit, I'm mad! Note that punctuation, capitalization, and spacing are usually ignored.'''

my_str=input('enter string:')
print(my_str)
new_str=''
for ch in my_str:
    if ch.isalpha():
        new_str+=ch

new_str=new_str.lower()
print(new_str)

if new_str==new_str[::-1]:
    print('Palindrome')
else:
    print('Not a palindrome')

#Another way
cleaned=[ch.lower() for ch in my_str if ch.isalpha()]
print(''.join(cleaned))
if cleaned==cleaned[::-1]:
    print('Palindrome')
else:
    print('Not a palindrome')
