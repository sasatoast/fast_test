from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/calculate/{sum_element1}/{sum_element2}")
async def calculate(sum_element1:int,sum_element2:int):
    sum_result=sum_element1+sum_element2
    return sum_result

@app.post("/calculate/sum")
async def calculate(sum_element1:int,sum_element2:int):
    sum_result=sum_element1+sum_element2
    return sum_result

