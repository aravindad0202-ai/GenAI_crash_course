from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

"""  EXAMPLE URL's
"https://www.youtube.com/watch?v=pVkDZueTBpY&list=RDMMpVkDZueTBpY&start_radio=1"
"https://en.wikipedia.org/wiki/Orange"
"""

@app.get('/home')
def hello():
    return 'THis is my first app'

@app.get('/users')
def user_details(name, company):
    res = {
        "name":name,
        "company":company
    }

    return JSONResponse(content=res, status_code=200)

# ------------------------------ POST ---------------------------------
class CompayVlidator(BaseModel):
    company: str
    name: str

@app.post('/company')
def company_details(request: CompayVlidator):
    company_dict ={
        "TCS":['Aravind', 'Anand'],
        "Infosys":['Sugumar', 'Vinoth']
    }
    company_details = request.company
    name_details = request.name

    for i,j in company_dict.items():
        if i == company_details:
            if name_details in j:
                db = 'available'
            else:
                db = 'not available'
            res = {
                'name':name_details,
                'company': company_details,
                'db_recorde':db
            }
    return JSONResponse(content=res, status_code=202)

