<script setup lang="ts">
import { Block } from '@/widget/Block';
import { Table } from '@/widget/Table';
import { getProbability, getFirstOrThrid, getFirstSec, getPairStat } from '../api';
import { combineProbabilities } from '../model';
import { onMounted, ref } from 'vue';

const dataTable = ref()
const dataTableTop = ref()


const func_get_probab = async () => {
    const respons = await getProbability();
    console.log(respons)

    dataTable.value = Object.entries(respons).map(([_, values], index) => {
  return {
    name: `Участник ${index + 1}`,
    probability: values.map((v: number) => v.toFixed(2))
  };
});
}

const func_get_FST = async () => {
    const respons = await getFirstOrThrid();
    const respons_2 = await getFirstSec();
    
    dataTableTop.value = combineProbabilities(respons,respons_2)
}

const func_get_pair_stat = async () => {
    const respons = await getPairStat();
    dataTableTwo.value = Object.entries(respons).map(([_, values], index) => {
    return {
        name: `Участник ${index + 1}`,
        probability: values.map((v: number) => v.toFixed(2))
    };
    });
}




const dataTableTwo = ref()

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


onMounted(() => {
    func_get_probab();
    func_get_FST();
    func_get_pair_stat();
})
</script>


<template>
    <div class="flex gap-10 mt-[40px] flex-wrap justify-between phone">
        <Block title="🏅Таблица вероятности по местам">
            <template #default>
                <Table :results="dataTable" :header="headTable" />
            </template>
        </Block>
        <Block title="🏅Таблица вероятности топ-2 и топ-3">
            <template #default>
                <Table :results="dataTableTop" :header="headTableTop" />
            </template>
        </Block>
        
        <Block title="🏅Таблица вероятности занятия 1го и 2го мест">
            <template #default>
                <Table :results="dataTableTwo" :header="headTableTwo" />
            </template>
        </Block>

        <Block title="🏁Статистика">
            <template #default>
                <Table :results="dataTableStat" :header="headTableStat" />
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