cards=('heart','spade','diamond','club')
for card in cards:
    print(card.upper())
print('diamond' in cards)
print('random' not in cards)
l_cards=list(cards)
l_cards.append('random')
cards=tuple(l_cards)

#Tuple Swapping
t1=(1,2,3)
t2=(10,20,30)
t1,t2=t2,t1
print(t1)
print(t2)

#zip
t3=('one','two','three')
zipped=tuple (zip(t1,t2,t3))
print(zipped)
print('-----------------------------------')
a,b,c=zipped
print(a)
for a,b,c in zipped:
    print(f'{a}, {b},{c}')