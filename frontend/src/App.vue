<script setup>
import { ref, onMounted } from 'vue'
import { listarProductos, crearProducto, eliminarProducto } from './api/productos'
import ProductoForm from './components/ProductoForm.vue'

const productos = ref([])
const cargando = ref(false)
const error = ref('')

async function cargar() {
  cargando.value = true
  error.value = ''
  try {
    productos.value = await listarProductos()
  } catch (e) {
    error.value = e.message
  } finally {
    cargando.value = false
  }
}

async function guardar(producto) {
  try {
    await crearProducto(producto)
    await cargar()
  } catch (e) {
    error.value = e.message
  }
}

async function borrar(id) {
  try {
    await eliminarProducto(id)
    await cargar()
  } catch (e) {
    error.value = e.message
  }
}

onMounted(cargar)
</script>

<template>
  <h1>Productos</h1>
  <ProductoForm @guardar="guardar" />

  <p v-if="cargando">Cargando...</p>
  <p v-else-if="error" style="color: red">{{ error }}</p>
  <p v-else-if="productos.length === 0">No hay productos.</p>
  <ul v-else>
    <li v-for="p in productos" :key="p.id">
      {{ p.nombre }} — ${{ p.precio }} ({{ p.stock }} unidades)
      <button @click="borrar(p.id)">Eliminar</button>
    </li>
  </ul>
</template>