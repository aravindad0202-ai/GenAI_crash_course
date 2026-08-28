from fastapi import FastAPI, Depends

app = FastAPI()

def loging():
    print('API is trigered')
    return "logg successfull"

@app.get('/home')
def home_function(a = Depends(loging)):
    print('Function invoked')
    print(a)
    return 'Successfull'