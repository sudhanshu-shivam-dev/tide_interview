from datetime import datetime as dt
present_year = int(dt.today().year)
import json 
import clearbit 
clearbit.key = 'sk_9ecea3c31cccffdce805f7a4c94c6cd6' 
company = dict(clearbit.Company.find(domain='tide.co',stream=True))
# print(company['tags'])
age = str(present_year - company['foundedYear'])+" Yrs"
emps = str(company['metrics']['employees'])
print(age,emps)
