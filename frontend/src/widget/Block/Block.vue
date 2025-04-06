<script setup lang="ts">
interface Props {
    title?: string;
    widht_block?: string
}

defineProps<Props>()

</script>


<template>
    <div v-if="!widht_block" class="max-w-[510px] w-full min-h-[250px] bg-figma-green rounded-[20px] p-3 text-white text-[20px] flex flex-col items-start">
        <p v-if="title">{{ title }}</p>
        <slot>

        </slot>
    </div>
    <div v-else class="w-full min-h-[250px] bg-figma-green rounded-[20px] p-3 text-white text-[20px] flex flex-col items-start" :style="{width: widht_block}">
        <p v-if="title" class="text-[30px]">{{ title }}</p>
        
        <slot>

        </slot>
    </div>
</template>
<style scoped>

</style>