from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
async def root():
    raise HTTPException(status_code=403, detail="Access Forbidden")

# For local development
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
