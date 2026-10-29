from fastapi import FastAPI

app = FastAPI()

from routes import auth_routes ,order_routes

app.include_router(auth_routes)
app.include_router(order_routes)

# para rodar o codigo no terminal: uvicorn main:app --reload(no mac usar python3 -m uvicorn main:app --reload)