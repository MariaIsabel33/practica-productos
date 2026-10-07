<script setup>
import { reactive } from 'vue'

const emit = defineEmits(['guardar'])
const form = reactive({ nombre: '', sku: '', precio: 0, stock: 0, categoria: 'ropa' })

function enviar() {
  emit('guardar', { ...form })
}
</script>

<template>
  <form @submit.prevent="enviar">
    <input v-model="form.nombre" placeholder="Nombre" />
    <input v-model="form.sku" placeholder="SKU" />
    <input v-model.number="form.precio" type="number" placeholder="Precio" />
    <input v-model.number="form.stock" type="number" placeholder="Stock" />
    <select v-model="form.categoria">
      <option>ropa</option>
      <option>tecnologia</option>
      <option>hogar</option>
    </select>
    <button>Guardar</button>
  </form>
</template>