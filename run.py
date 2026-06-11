import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
from dotenv import load_dotenv
load_dotenv()


app = FastAPI()
counter = os.getenv("COUNTER")
counter = 0

@app.get("/")
def read_root():
    return JSONResponse({"Hello": "World"})

@app.get("/count")
def main():
    global counter
    counter = (counter)
    counter += 1
    return JSONResponse(
        { 
            "status": 200,
            "response": f"I have seen {counter} times.\n",
        }
    )
@app.get("/color")
def get_color():
    load_dotenv()
    color = os.getenv("COLOR")
    return JSONResponse(
        {
            "status" :200,
            "response" : "My color is {} ".format(
                str(color),
            ),
        },
    )


if __name__ == "__main__":
    uvicorn.run(
        "run:app",
        host="0.0.0.0",
        port=2010,
        reload=False,
    )
