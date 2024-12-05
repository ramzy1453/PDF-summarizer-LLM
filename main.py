from fastapi import FastAPI
import uvicorn

from app.routers.pdf import router as pdf_router

app = FastAPI(debug=True)

@app.get("/")
def api():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    return {"item_id": item_id}


app.include_router(pdf_router, prefix="/api/v1/pdf", tags=["pdf"])

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=7000)