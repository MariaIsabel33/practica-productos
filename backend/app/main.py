from fastapi import FastAPI
from .db import get_conn

app = FastAPI()

@app.get("/productos")
def listar_productos():
    with get_conn() as conn:
        return conn.execute("SELECT * FROM productos ORDER BY id").fetchall()