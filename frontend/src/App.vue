<script setup>
import { ref, onMounted } from 'vue'
import { listarProductos } from './api/productos'

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

onMounted(cargar)
</script>

<template>
  <h1>Productos</h1>

  <p v-if="cargando">Cargando...</p>
  <p v-else-if="error" style="color: red">{{ error }}</p>
  <p v-else-if="productos.length === 0">No hay productos.</p>

  <ul v-else>
    <li v-for="p in productos" :key="p.id">
      {{ p.nombre }} — ${{ p.precio }} ({{ p.stock }} unidades)
    </li>
  </ul>
</template>