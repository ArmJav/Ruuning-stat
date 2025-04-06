<script setup lang="ts">
import { Block } from '@/widget/Block';
import { ref } from 'vue';
import { LoadingOutlined, DeleteOutlined } from '@ant-design/icons-vue';
import runner_svg from '@/assets/runner_svg.vue';
import runnersvg_2 from '@/assets/runnersvg_2.vue';
import { message } from 'ant-design-vue';
interface Runner {
    id: number
    name: string
    key: keyof typeof runners_data.value
    position: number
    color: string
}
const loading_running = ref<boolean>(false)
const runners_data = ref({
    runner_one: 0,
    runner_two: 0,
    runner_three: 0,
    runner_four: 0,
    runner_five: 0,
    runner_six: 0
}

)

const runners = ref<Runner[]>([
    { id: 1, name: 'У1', key: 'runner_one', position: 0, color: '#FF6B6B' },
    { id: 2, name: 'У2', key: 'runner_two', position: 0, color: '#4ECDC4' },
    { id: 3, name: 'У3', key: 'runner_three', position: 0, color: '#FFD93D' },
    { id: 4, name: 'У4', key: 'runner_four', position: 0, color: '#1A759F' },
    { id: 5, name: 'У5', key: 'runner_five', position: 0, color: '#A8DADC' },
    { id: 6, name: 'У6', key: 'runner_six', position: 0, color: '#F28482' }
])

const resetProgress = () => {
    runners_data.value = {
        runner_one: 0,
        runner_two: 0,
        runner_three: 0,
        runner_four: 0,
        runner_five: 0,
        runner_six: 0
    }
}

const startRace = () => {
    loading_running.value = true
    const interval = setInterval(() => {
        let allFinished = true
        runners.value.forEach((runner) => {
            if (runner.position < 100) {
                runner.position += Math.random() * 4
                runner.position = Math.min(runner.position, 100)
                runners_data.value[runner.key] = runner.position
                allFinished = false
            }

        })
        if (allFinished) {
            clearInterval(interval)
            loading_running.value = false
            message.success('Гонка окончен')

        }
    }, 1000)
}

</script>

<template>
    <div class="py-[20px] flex flex-col gap-3 items-start">
        <div class="flex justify-center gap-3 items-center">
            <button v-if="!loading_running" @click="startRace"
                class="bg-[#29A851] h-[40px] w-[240px] text-white rounded-[15px] cursor-pointer hover:opacity-35 active:bg-[#5CD683] active:opacity-100 transition duration-300  ">
                ВКЛЮЧИТЬ СИМУЛЯЦИЮ
            </button>

            <button v-else
                class="bg-[#007b94] h-[40px] w-[240px] text-white rounded-[15px] flex items-center justify-center gap-1">
                <loading-outlined />
                <p>СИМУЛЯЦИЯ</p>
            </button>

            <div @click="resetProgress" class="flex items-center gap-2 text-gray-500 h-fit cursor-pointer">
                <p>СБРОС</p>
                <DeleteOutlined />
            </div>
        </div>

        <Block title="Атлет" widht_block='100%'>
            <template #default>
                <div class="flex bg-[#f1f1f1] rounded-[10px] w-full p-2">
                    <div class="text-[16px] flex flex-col gap-[30px] w-fit min-w-[120px]">
                        <div>
                            <p class="text-red-500">УЧАСТНИК 1</p>
                            <a-divider style="background-color: black; margin-block: 2px"></a-divider>
                        </div>
                        <div>
                            <p class="text-pink-400">УЧАСТНИК 2</p>
                            <a-divider style="background-color: black; margin-block: 2px"></a-divider>
                        </div>
                        <div>
                            <p class="text-blue-400">УЧАСТНИК 3</p>
                            <a-divider style="background-color: black; margin-block: 2px"></a-divider>

                        </div>
                        <div>
                            <p class="text-orange-400">УЧАСТНИК 4</p>
                            <a-divider style="background-color: black; margin-block: 2px"></a-divider>
                        </div>
                        <div>
                            <p class="text-green-400">УЧАСТНИК 5</p>
                            <a-divider style="background-color: black; margin-block: 2px"></a-divider>
                        </div>
                        <div>
                            <p class="text-blue-700">УЧАСТНИК 6</p>
                            <a-divider style="background-color: black; margin-block: 2px"></a-divider>
                        </div>
                    </div>
                    <a-divider type="vertical" style="height: 320px; width: 2px; background-color: black;"></a-divider>
                    <div class="w-full h-full flex flex-col gap-[30px] relative">
                        <div class="runner h-[28px] bg-[#CF1322] transition-width"
                            :style="{ width: String(runners_data.runner_one) + '%' }">
                            <runnersvg_2 class="w-fit h-[28px] absolute transition-left" color="#CF1322"
                            :style="{ left: String(runners_data.runner_one) + '%' }" />
                        </div>

                        <div class="runner h-[28px] bg-[#C4218A]"
                            :style="{ width: String(runners_data.runner_two) + '%' }">
                            <runnersvg_2 class="w-fit h-[28px] absolute" color="#C4218A"
                            :style="{ left: String(runners_data.runner_two) + '%' }" />
                        </div>

                        <div class="runner h-[28px] bg-[#08A4C4]"
                            :style="{ width: String(runners_data.runner_three) + '%'}">
                            <runnersvg_2 class="w-fit h-[28px] absolute" color="#08A4C4"
                            :style="{ left: String(runners_data.runner_three) + '%' }" />
                        </div>

                        <div class="runner h-[28px] bg-[#D78739]"
                            :style="{ width: String(runners_data.runner_four) + '%' }">
                            <runnersvg_2 class="w-fit h-[28px] absolute" color="#D78739"
                            :style="{ left: String(runners_data.runner_four) + '%' }" />
                        </div>

                        <div class="runner h-[28px] bg-green-400"
                            :style="{ width: String(runners_data.runner_five) + '%' }">
                            <runnersvg_2 class="w-fit h-[28px] absolute" color="#05df72"
                            :style="{ left: String(runners_data.runner_five) + '%' }" />
                        </div>

                        <div class="runner h-[28px] bg-blue-700"
                            :style="{ width: String(runners_data.runner_six) + '%' }">
                            <runnersvg_2 class="w-fit h-[28px] absolute" color="#1447e6"
                            :style="{ left: String(runners_data.runner_six) + '%' }" />
                        </div>
                    </div>

                    <a-divider type="vertical" style="height: 320px; width: 1px; background-color: black; margin: 0"></a-divider>
                    <div class="vertical-rl text-2xl text-gray-500 text-center w-25 flex justify-center items-center">
                        <p>ФИНИШ</p>
                    </div>

                </div>
            </template>

        </Block>
    </div>
</template>

<style scoped>
.race-track {
    position: relative;

    width: 100%;
    height: 200px;
    background: #f0f0f0;
    border: 1px solid #ccc;
}

.runner {
    width: 60px;
    text-align: end;
    border-radius: 0 10px 10px 0;
    font-weight: bold;
}
</style>