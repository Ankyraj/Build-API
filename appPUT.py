from fastapi import FastAPI 
from pydantic import BaseModel  ## To protect the data that we are passing with URL 


class Input(BaseModel):
    age : int 
    sex : str
    
    
app = FastAPI()

@app.put("/predict")
def predict_model(d: Input) :
    if d.age < 10 or d.sex == 'F': 
        return {'survived':1}
    else:
        return {'survived': 0}