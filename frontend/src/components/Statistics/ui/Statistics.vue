<script setup lang="ts">
import { Block } from '@/widget/Block';
import { Table } from '@/widget/Table';

const dataTable = [
    { name: 'Участник 1', probability: ['0.5', '0.2', '0.1', '0.2', '0.2', '0.9'] },
    { name: 'Участник 2', probability: ['0.51', '0.21', '0.11', '0.21', '0.2'] },
    { name: 'Участник 3', probability: ['0.53', '0.23', '0.13', '0.23', '0.2'] },
    { name: 'Участник 4', probability: ['0.5', '0.2', '0.1', '0.2', '0.2'] },
    { name: 'Участник 5', probability: ['0.51', '0.21', '0.11', '0.21', '0.2'] },
    { name: 'Участник 6', probability: ['0.53', '0.23', '0.13', '0.23', '0.2'] },

]

const dataTableTop = [
    { name: 'Участник 1', probability: ['0.5', '0.2',] },
    { name: 'Участник 2', probability: ['0.51', '0.21',] },
    { name: 'Участник 3', probability: ['0.53', '0.23',] },
    { name: 'Участник 4', probability: ['0.5', '0.2',] },
    { name: 'Участник 5', probability: ['0.51', '0.21', ] },
    { name: 'Участник 6', probability: ['0.53', '0.23', ] },

]

const dataTableTwo = [
    { name: 'Участник 1', probability: ['0.5', '0.2', '0.1', '0.2', '0.2', '0.9'] },
    { name: 'Участник 2', probability: ['0.51', '0.21', '0.11', '0.21', '0.2'] },
    { name: 'Участник 3', probability: ['0.53', '0.23', '0.13', '0.23', '0.2'] },
    { name: 'Участник 4', probability: ['0.5', '0.2', '0.1', '0.2', '0.2'] },
    { name: 'Участник 5', probability: ['0.51', '0.21', '0.11', '0.21', '0.2'] },
    { name: 'Участник 6', probability: ['0.53', '0.23', '0.13', '0.23', '0.2'] },
]

const dataTableStat = [
    { name: 'Участник 1', probability: ['1', '1', '2', '3', '4', '5', '6', '3', '5', '2'] },
    { name: 'Участник 2', probability: ['1', '1', '2', '3', '4', '5', '6', '3', '5', '2'] },
    { name: 'Участник 3', probability: ['1', '1', '2', '3', '4', '5', '6', '3', '5', '2'] },
    { name: 'Участник 4', probability: ['1', '1', '2', '3', '4', '5', '6', '3', '5', '2'] },
    { name: 'Участник 5', probability: ['1', '1', '2', '3', '4', '5', '6', '3', '5', '2'] },
    { name: 'Участник 6', probability: ['1', '1', '2', '3', '4', '5', '6', '3', '5', '2'] },
]


const headTable = ['Атлет', '🏆1 место', '🥈2 место', '🥉3 место', '4 место', '5 место', '6 место']
const headTableTop = ['Атлет', '🏆 Топ 1-2 место', '🥈 Топ 1-3 место']
const headTableTwo = ['Атлет', 'УЧ.1', 'УЧ.2', 'УЧ.3', 'УЧ.4', 'УЧ.5', 'УЧ.6' ]
const headTableStat = ['Забег', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10' ]
</script>


<template>
    <div class="flex gap-10 mt-[40px] flex-wrap justify-between phone">
        <Block title="🏅Таблица вероятности по местам">
            <template #default>
                <Table :results="dataTable" :header="headTable" />
            </template>
        </Block>
        <Block title="🏅Таблица вероятности топ 2 или топ 3">
            <template #default>
                <Table :results="dataTableTop" :header="headTableTop" />
            </template>
        </Block>
        <Block title="🏁Статистика">
            <template #default>
                <Table :results="dataTableStat" :header="headTableStat" />
            </template>
        </Block>
        <Block title="🏅Таблица вероятности занятия 1го и 2го мест">
            <template #default>
                <Table :results="dataTableTwo" :header="headTableTwo" />
            </template>
        </Block>

    </div>
</template>
<style scoped>
@media (max-width: 510px) {
    .phone {
        margin-inline: 0;
    }
}
</style>