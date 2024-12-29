import uvicorn
from fastapi import FastAPI
from routers import user, task


app = FastAPI()

@app.get('/')
async def welcome() -> dict:
    return {"message": "Welcome to Taskmanager"}

app.include_router(user.router)
app.include_router(task.router)

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
