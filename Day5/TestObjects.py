from CarPortal import Car

c1=Car('Honda','Elevate',200000)
c2=Car('Tata','nexon',450000)

print(c1.make)
c1._make='abcd'
print(c1)

#c1.make="abcd"  #AttributeError- because field is read only
#c1.price=0  #ValueError('Price should be positive')
c1._price=0
print(c1)

# print(c1.calculate_premium(2))
# print(c1.calculate_premium(2))

print(c1)
c3=eval(repr(c1))
print(c3)

# Car.show_count()

c4=Car.from_string("tata,nexon,1400000")
print(type(c4))
print(c4)