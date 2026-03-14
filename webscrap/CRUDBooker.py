import requests as req

res=req.post('https://restful-booker.herokuapp.com/booking')
print(res.status_code)



