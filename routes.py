from fastapi import APIRouter
import sqlite3
from models import db, cursor

auth_routes = APIRouter(prefix="/auth", tags=["autenticaçao"])
order_routes = APIRouter(prefix="/pedidos", tags=["pedidos"])

@auth_routes.get("/")
async def autorizações():
    return {"mensagem: voçê acessou a rota de autorização"} 

@order_routes.get("/")
async def pedidos():
    return {"Mensagem: voçê acessou a rota de pedidos"}

@auth_routes.post("/criar conta")
async def register(email: str, senha: str, nome: str):
     db.row_factory = sqlite3.Row
     cursor.execute(email,)
     usuario = cursor.fetchone()
     if usuario:
         db.close
         return {"O usuario já existe"}
     else:
         cursor.execute(nome, email, senha)
         db.commit
         db.close
         return {"O usuario foi criado com sucesso"}