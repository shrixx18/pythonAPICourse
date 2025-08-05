# to run the server use the command => uvicorn main:app --reload
from fastapi import FastAPI
from fastapi import Body
app = FastAPI()


@app.get("/")                         # decorator , with an http get method
async def root():                     # a normal function with an extra keyword async, its for asynchronous functionality
    return "Helooo from Shriii # !!"    #


@app.get("/posts")
def get_posts():
    return {"data": "Here comes your data"}


@app.post("/createposts")
def create_post(payLoad: dict = Body(...)):
    print(payLoad)
    return {"new_post": f" title {payLoad['title']} content {payLoad['body']}"}
