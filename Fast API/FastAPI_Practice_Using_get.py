# Import the FastAPI library
from fastapi import FastAPI

# Create a FastAPI application
app = FastAPI()
# Call FastAPI using Pydantic
@app.get("/")
async def read_main():
    msg = "Welcome to Geeks For Geeks"
    test_msg = "Welcome to Geeks For Geeks"
    if msg == test_msg:
        return {"msg": "Test Passed"}
    else:
        return {"msg": "Test Failed"}
