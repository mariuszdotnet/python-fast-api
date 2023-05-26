from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Super Mario World 2"}

if __name__ == '__main__':
    uvicorn.run('main:app')