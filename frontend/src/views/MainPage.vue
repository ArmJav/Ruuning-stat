<script setup lang="ts">
import { Headers } from '@/widget/Headers';
import { Statistics } from '@/components/Statistics';
import { Running } from '@/components/Running';
</script>

<template>
    <Headers/>
    <div class="mx-[70px] phone">
        <p class="text-white mx-auto mt-10 text-center text-[30px]">ПОДРОБНАЯ СТАТИСТИКА ЗАБЕГОВ</p>
        <Statistics/>
        <p class="text-white mx-auto mt-10 text-center text-[30px]">LIVE-ТРАНСЛЯЦИЯ ЗАБЕГА</p>
        <Running/>
    </div>
    
</template>

<style scoped>
@media (max-width: 510px) {
    .phone {
        margin-inline: auto;
    }
}

</style>