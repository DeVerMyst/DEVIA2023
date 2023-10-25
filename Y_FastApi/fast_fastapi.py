from fastapi import FastAPI

app = FastAPI()

@app.get("/endpoint")
def read_data():
    return {"method": "GET"}

@app.post("/endpoint")
def create_data():
    return {"method": "POST"}

@app.put("/endpoint")
def update_data():
    return {"method": "PUT"}

@app.delete("/endpoint")
def delete_data():
    return {"method": "DELETE"}