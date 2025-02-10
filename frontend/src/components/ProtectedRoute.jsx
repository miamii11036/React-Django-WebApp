import { Navigate } from "react-router-dom";
import { jwtDecode } from "jwt-decode";
import api from "../api";
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants";
import { useEffect, useState } from "react";

function ProtectedRoute({ children }) {
    const [isAuthorized, setIsAuthorized] = useState(null);

    useEffect(() => { 
        auth().catch(()=> setIsAuthorized(false));
        //auth函數返回Promise的異步函數，為了執行身份驗證，若驗證失敗則執行catch區塊內的函數
    }, []); //空陣列[]作為useEffect的依賴陣列，表示這個效果只在組件首次掛載時執行一次，防止auth函數重複執行

    const refreshToken = async () => {
    //重新取得token
    const refreshToken = localStorage.getItem(REFRESH_TOKEN); //取得refreshToken
    try {
      //向後端發送request
      const res = await api.post("/api/token/refresh/", {
        //向 /api/token/refresh/ API傳送refreshToken並等待回應取得新的accessToken
        refresh: refreshToken,
      }); 
      if (res.status === 200) {
        localStorage.setItem(ACCESS_TOKEN, res.data.access); //將新的accessToken存入本地
        setIsAuthorized(true); 
      } else {
        setIsAuthorized(false); 
      }
    } catch (error) {
      console.error(error);
      setIsAuthorized(false);
    }
  };

    const auth = async () => {
    //驗證token是否過期
    const token = localStorage.getItem(ACCESS_TOKEN);
    if (!token) {
      //如果token不存在
      setIsAuthorized(false); //設定為未授權
    }

    const decoded = jwtDecode(token); //解碼token
    const tokenExpiration = decoded.exp * 1000; //取得token過期日期
    const now = Date.now(); //取得現在時間

    if (tokenExpiration < now) {
      //如果token過期
      await refreshToken(); //重新取得token
    } else {
      setIsAuthorized(true); //設定為已授權
    }
  };

    if (isAuthorized === null) {
        return <div>Loading...</div>;
  }
  return isAuthorized ? children : <Navigate to="/login" />;
}

export default ProtectedRoute;
