from imp import reload
from unittest import result
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


from anyio import from_thread, sleep, to_thread, run

app = FastAPI()

origins = ["*"]

in_use = 0

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def long_func(s):
    print(s)
    count = 0
    for i in range(100000000):
        count += i
    return count 



def blocking_function(tweet):
    # result=from_thread.run(long_func, tweet)
    result=long_func(tweet)
    print(tweet, result)
    global in_use
    in_use -= 1
    return result
        

@app.get("/promo_comments/")
async def run_async(tweet: str):
    global in_use
    if in_use < 2:
        in_use += 1
        return await to_thread.run_sync(blocking_function,tweet)
    else:
        return "nikal"

   
    

    
if __name__ == '__main__':
    uvicorn.run(app, port=8083, host='0.0.0.0')
