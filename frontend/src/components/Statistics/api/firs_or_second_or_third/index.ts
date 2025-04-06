import { AxiosError } from "axios";
import { ApiClient } from "@/api/Client";

interface ResponseBody {
    pl1: number[] | null,
    pl2: number[] | null,
    pl3: number[] | null,
    pl4: number[] | null,
    pl5: number[] | null,
    pl6: number[] | null,
    
  }
  
  export const getFirstOrSecond = async (): Promise<ResponseBody> => {
    try {
      const { data: response } = await ApiClient({
        method: "GET",
        url: `first_or_second_or_third`,
      });
  

      return response
    } catch (error: unknown) {
      // Проверяем, является ли ошибка экземпляром AxiosError
      if (error instanceof AxiosError) {
        console.error("Ошибка при отправлении запроса", error.message);
        return {pl1: null, pl2: null, pl3: null, pl4: null, pl5: null, pl6: null};
      } else {
        // Обработка неизвестной ошибки
        console.error("Неизвестная ошибка при отправлении запроса:", error);
        return {pl1: null, pl2: null, pl3: null, pl4: null, pl5: null, pl6: null};
      }
    }
  };
  