import pandas as pd
import requests as req

res=req.get('https://api.restful-api.dev/objects')
print(res.status_code)
response=res.json()
product_list=[]

for item in response:
    data={'id':item['id'], 'name':item['name']}
    if item['data']:
        data.update(item['data'])
    product_list.append(data)

df=pd.DataFrame(product_list)
df.to_csv('Product_data.csv')


print('--------------------------------------------')
'''send query params as list of tuples
containing param name - value'''
params=[('id',5),('id',7),('id',10)]
res=req.get('https://api.restful-api.dev/objects',params=params)
print(res.status_code)
response=res.json()
print(response)

print('--------------------------------------------')
'''send path params to retrieve one resource uniquely'''
p_id=7
res=req.get(f'https://api.restful-api.dev/objects/{p_id}')
print(res.status_code)
response=res.json()
print(response)