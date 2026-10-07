# Gestión de productos

Aplicación web con API en FastAPI, frontend en Vue 3 (Composition API) y PostgreSQL.

## Requisitos
- Python 3.11+
- Node.js 20+
- PostgreSQL 15+

## 1. Base de datos
```
createdb -U postgres tienda
psql -U postgres -d tienda -f db/schema.sql
```

## 2. Backend
```
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```
Copiar `.env.example` como `.env` y ajustar la contraseña. Luego:
```
uvicorn app.main:app --reload
```
API en http://localhost:8000 y documentación en http://localhost:8000/docs

## 3. Frontend
```
cd frontend
npm install
npm run dev
```
Crear `frontend/.env` con `VITE_API_URL=http://localhost:8000`.
Disponible en http://localhost:5173

## Pendientes y mejoras
- Editar productos desde la interfaz (el endpoint PUT ya existe en la API).
- Mostrar en el formulario los errores de validación campo por campo.
- Paginación del listado.
- Pruebas automatizadas con pytest.
- Docker Compose para levantar todo con un comando.