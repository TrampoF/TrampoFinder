import axios, {AxiosInstance} from "axios";

export const api: AxiosInstance = axios.create({
    baseURL: process.env.JOB_BOARD_API_URL,
    headers: {
        'Content-Type': "application/json"
    }
})