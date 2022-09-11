import requests



# key = '3VPJYVRtmTQuh0ydjWDAX90E3LcDxQyV'

url = f"https://api.apilayer.com/fixer/latest?base=USD&symbols=EUR,GBP&apikey=3VPJYVRtmTQuh0ydjWDAX90E3LcDxQyV"


print("waiting for server response ... ")
res = requests.get( url )
data = res.json()
# print(data)
print()
print("EUR/USD = ",data['rates']['EUR'])
print("GBP/USD = ",data['rates']['GBP'])
print()
