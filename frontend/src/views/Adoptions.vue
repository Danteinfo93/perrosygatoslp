<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Adopciones"/>
    <ListAdoption/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import ListAdoption from '@/components/Adoption/ListAdoption.vue'

export default {
  name: 'home',
  components: {
    HelloWorld,
    ListAdoption
  }
}
</script>
