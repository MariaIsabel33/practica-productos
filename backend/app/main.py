from fastapi import FastAPI, HTTPException
from psycopg import errors
from .db import get_conn
from .schemas import ProductoIn

app = FastAPI()

@app.get("/productos")
def listar_productos():
    with get_conn() as conn:
        return conn.execute("SELECT * FROM productos ORDER BY id").fetchall()

@app.post("/productos", status_code=201)
def crear_producto(producto: ProductoIn):
    try:
        with get_conn() as conn:
            return conn.execute(
                """
                INSERT INTO productos (nombre, sku, precio, stock, categoria)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING *
                """,
                (producto.nombre, producto.sku, producto.precio, producto.stock, producto.categoria),
            ).fetchone()
    except errors.UniqueViolation:
        raise HTTPException(status_code=409, detail="Ya existe un producto con ese SKU")
    except errors.CheckViolation:
        raise HTTPException(status_code=400, detail="Los datos no cumplen las reglas de la base de datos")