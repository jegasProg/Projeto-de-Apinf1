from fastapi import APIRouter

auth_routes = APIRouter(prefix="/auth", tags=["autenticaçao"])
order_routes = APIRouter(prefix="/pedidos", tags=["pedidos"])