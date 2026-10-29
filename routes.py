from fastapi import APIRouter

auth_routes = APIRouter(prefix="/auth", tags=["autenticaçao"])
order_routes = APIRouter(prefix="/pedidos", tags=["pedidos"])

@auth_routes.get("/")
async def pedidos():
    return {"mensagem: voçê acessou a rota de pedidos"} 