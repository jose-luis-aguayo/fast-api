from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    print(item)
    return {"msg": "item created"}


@app.get("/")
async def root():
    return {"message": "hello world"}

@app.get("/items/{item_id}")
async def get_item(item_id):
    return {"item": f"the item id is: {item_id}"}

'''
Will throw the following error if passing a value different than int
{"detail":[{"type":"int_parsing","loc":["path","number"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"w"}]}
'''
@app.get("/validation/{number}") #this is a path parameter
async def validate(number: int):
    return {"Number": f"your integer {number}"} 


#optional parameters
@app.get("/optional/")
async def optional(my_param: str, q: str | None = None): #expecting to be query parameter
    if q:
        return {"Your values": f"param: {my_param}, q {q}"}
    else:
        return {"param": f"param {my_param}"}
    
#testing query parameters with default value
@app.get("/query-params/")
async def query_parameters(p_1: str = "a", p_2: str = "b"):
    return {
        "p_1": p_1,
        "p_2": p_2
    }    