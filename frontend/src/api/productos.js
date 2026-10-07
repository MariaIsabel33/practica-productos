const BASE = import.meta.env.VITE_API_URL

async function request(path, options = {}) {
  const res = await fetch(`${BASE}${path}`, {
    headers: { 'Content-Type': 'application/json' },
    ...options,
  })
  if (res.status === 204) return null
  const data = await res.json().catch(() => null)
  if (!res.ok) {
    throw new Error(typeof data?.detail === 'string' ? data.detail : 'Datos inválidos')
  }
  return data
}

export const listarProductos = () => request('/productos')
export const crearProducto = (p) => request('/productos', { method: 'POST', body: JSON.stringify(p) })
export const eliminarProducto = (id) => request(`/productos/${id}`, { method: 'DELETE' })