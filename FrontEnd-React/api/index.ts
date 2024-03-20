import {api} from "./config";
import {AxiosResponse} from "axios";

export const index = async (): Promise<AxiosResponse> => {
    return await api.get("/api/index")
}