export interface ResponseBody {
    pl1: number[] | null,
    pl2: number[] | null,
    pl3: number[] | null,
    pl4: number[] | null,
    pl5: number[] | null,
    pl6: number[] | null,
    
  }
  interface Participant {
    name: string;
    probability: string[];
}

  export function combineProbabilities(prob1: Record<string, number>, prob2: Record<string, number>): Participant[] {
    const result: Participant[] = [];

    for (let i = 1; i <= 6; i++) {
        const key = `pl${i}`;
        result.push({
            name: `Участник ${i}`,
            probability: [
                prob1[key].toFixed(2), // Форматируем до двух знаков
                prob2[key].toFixed(2)  // Форматируем до двух знаков
            ]
        });
    }

    return result;
}