from datetime import datetime as dt
import asyncio

import json 
import clearbit 
from model import Company
async def fetch_company_details_and_persist(name, domain):
    company_details_clearbit = dict(clearbit.Company.find(domain='tide.co',stream=True))
    present_year = int(dt.today().year)
    age = str(present_year - company['foundedYear'])+" Yrs"
    emps = str(company['metrics']['employees'])
    company = Company(name=name, domain=domain, age=age, emps=emps)
    
    return 
 

async def send_ack_as(name, domain):
    task = asyncio.create_task(fetch_company_details_and_persist(name, domain))
    return {'status': 'Your request has been received'}
def send_ack_m(name, domain):
    asyncio.run(send_ack_as(name, domain))
    
