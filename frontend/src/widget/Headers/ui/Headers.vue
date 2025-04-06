<script setup lang="ts">
import logo from '@/assets/logo.png'
import router from "@/router";


</script>

<template>
  <div class="flex justify-between items-center text-white text-[25px] mx-[50px] phone">
    <div>
      <img :src="logo" alt="" class="max-w-[150px] max-h-[25px]">
      <!-- <h1 class="text-figma-green">Vuetopia</h1> -->

    </div>
    <p class="cursor-pointer text-shadow-xs text-[25px]">ХАРАКТЕРИСТИКА</p>
  </div>
  <a-divider class="bg-white" style="margin-block: 10px;"></a-divider>

</template>

<style scoped>
@media (max-width: 510px) {
    .phone {
        margin-inline: 0;
    }
}
</style>