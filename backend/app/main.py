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

@app.get("/productos/{producto_id}")
def obtener_producto(producto_id: int):
    with get_conn() as conn:
        producto = conn.execute(
            "SELECT * FROM productos WHERE id = %s", (producto_id,)
        ).fetchone()
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto


@app.put("/productos/{producto_id}")
def actualizar_producto(producto_id: int, producto: ProductoIn):
    try:
        with get_conn() as conn:
            actualizado = conn.execute(
                """
                UPDATE productos
                SET nombre = %s, sku = %s, precio = %s, stock = %s, categoria = %s
                WHERE id = %s
                RETURNING *
                """,
                (producto.nombre, producto.sku, producto.precio,
                 producto.stock, producto.categoria, producto_id),
            ).fetchone()
    except errors.UniqueViolation:
        raise HTTPException(status_code=409, detail="Ya existe un producto con ese SKU")
    if actualizado is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return actualizado


@app.delete("/productos/{producto_id}", status_code=204)
def eliminar_producto(producto_id: int):
    with get_conn() as conn:
        resultado = conn.execute(
            "DELETE FROM productos WHERE id = %s", (producto_id,)
        )
    if resultado.rowcount == 0:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    