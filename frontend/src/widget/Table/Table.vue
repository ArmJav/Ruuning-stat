<script setup lang="ts">
import { computed, ref } from 'vue';


interface TableData {
    name: string,
    probability: string[]
}
interface Props {
    results: TableData[],
    header: string[]
}


const color_dist: Record<string, string> = {
    "Участник 1": "red",
    "Участник 2": "pink",
    "Участник 3": "cyan",
    "Участник 4": "orange",
    "Участник 5": "green",
    "Участник 6": "blue",
}

const getRunnerColor = (name: string) => {
    return color_dist[name]
}

const { results } = defineProps<Props>()
</script>

<template>
    <div class="max-w-[490px] font-display w-full bg-white h-full rounded-xl font-medium border border-gray-200  shadow ">
        <div class="overflow-x-auto rounded-xl">
            <table class="min-w-full text-[12px] text-left">
                <thead class="bg-gray-100 text-gray-700 text-center">
                    <tr>
                        <th class="py-[2px] px-1" v-for="(title, index) in header" :key="index">
                            <p>
                                {{ title }}
                            </p>
                        </th>
                    </tr>
                </thead>
                <tbody class="text-grey text-[12px] font-sans text-center mb-2">
                    <tr v-for="(runner, index) in results" :key="runner.name" class="hover:bg-gray-50 border border-gray-200">
                        <!-- <td class="py-[1px] px-[2px]">{{ runner.name }}</td> -->
                        <td class="py-[3px] px-[3px]">
                            <a-tag :color="getRunnerColor(runner.name)">{{ runner.name }}</a-tag>
                        </td>
                        <td class="py-[1px] px-[2px]" v-for="prob in runner.probability">
                            <p>{{ prob }}</p>
                        </td>

                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>