from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

app = FastAPI()

company_dict ={
        "TCS":['Aravind', 'Anand'],
        "Infosys":['Sugumar', 'Vinoth']
    }

class CompayVlidator(BaseModel):
    company: str
    name: str

@app.get('/company')
def user_details(company):
    res = {
        'user_details':company_dict[company]
    }
    return JSONResponse(content=res, status_code=200)

@app.post('/company')
def company_details(request: CompayVlidator): # Create new company
    company = request.company
    name = request.name

    if company in company_dict:
        return JSONResponse(content = {'error':f'{company} already exists in database.'}) 
    else:
        company_dict[company] = [name]
        return JSONResponse(content=company_dict, status_code=202)

@app.patch('/company')
def update_details(request: CompayVlidator):
    company = request.company
    name = request.name

    if company in company_dict:
        company_dict[company].append(name)

        return JSONResponse(content = {'message':'User added successfully', 'db':company_dict}, status_code=200)
    else:
        return JSONResponse(content = {'error':f'{company} is not in database'})

@app.put('/company')
def edit_details(request: CompayVlidator):
    company = request.company
    name = request.name

    if company in company_dict:
        company_dict[company] = [name]
        return JSONResponse(content = {'message':'User added successfully', 'db':company_dict}, status_code=200)
    
    else:
        return JSONResponse(content = {'error':f'{company} is not in database'})


# ------------------------------------------------------- SERIALIZER EXPLAINATION ------------------------------------------------------
"""COde given below is only to understand the concept of how serialization work
There is no relationship between this concept and the above project
"""

class RequestValidator(BaseModel):
    banckaount : int
    name: str
    amount: int = Field(gt=0, le=10000)

class ResponseValidator(BaseModel):
    status: str
    amount: int

@app.post('/learning')
def learn_serializer(request: RequestValidator):
    print("working")
    res_obj = ResponseValidator(status = "Good", amount=request.amount)
    return JSONResponse(content=res_obj, status_code=200)
    # brokne_res = {'status':'good',"amount":request.amount}
    # return brokne_res