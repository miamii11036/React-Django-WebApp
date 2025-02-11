/*axios作為攔截器，會攔截前端傳送的任何request，並自動新增header */
import axios from 'axios'; //會檢查每一個傳送的request是否有token，如果有就會自動加上header
import { ACCESS_TOKEN } from './constants';

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL   //用於import前端.env檔案中的變數
});

api.interceptors.request.use( //啟動axios的requests攔截器
    (config) => { //攔截器成功攔截
        const accessToken = localStorage.getItem(ACCESS_TOKEN); //從前端本地取得accessToken
        if (accessToken) { 
            config.headers.Authorization = `Bearer ${accessToken}`; //將accessToken加入加密的HTTPheader by Authorization
        }                                   //Bearer是OAuth 2.0的一種身份驗證格式，代表持有者憑證 
        return config;
    },
    (error) => { //攔截器失敗攔截
        return Promise.reject(error);
    }
);

export default api; 