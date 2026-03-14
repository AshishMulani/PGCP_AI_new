import pandas as pd
import requests as req

res=req.get('https://restful-booker.herokuapp.com/booking')
print(res.status_code)
response=res.json()
data_list=[]

for item in response:
    data = {'bookingid': item['bookingid']}
    # data={'firstname':item['firstname'], 'lastname':item['lastname'],
    #       'totalprice':item['totalprice'], 'depositpaid':item['depositpaid'],
    #        'additionalneeds':item['additionalneeds']}

    # if item['bookingdates']:
    #     data.update(item['bookingdates'])
    data_list.append(data)

df = pd.DataFrame(data_list)
df.to_csv('Product_data.csv')


print('--------------------------------------------')
'''send query params as list of tuples
containing param name - value'''
# params=[('bookingid',5),('bookingid',7),('bookingid',10)]
res=req.get('https://restful-booker.herokuapp.com/booking?firstname=sally&lastname=brown')
print(res.status_code)
response=res.json()
print(response)

print('--------------------------------------------')
'''send path params to retrieve one resource uniquely'''
p_id=7
res=req.get(f'https://restful-booker.herokuapp.com/booking/{p_id}')
print(res.status_code)
response=res.json()
print(response)

print('--------------------------------------------')

# p_id=7
res=req.get('https://restful-booker.herokuapp.com/booking/10')
print(res.status_code)
response=res.json()
print(response)

print('--------------------------------------------')


