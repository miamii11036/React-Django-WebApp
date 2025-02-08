from django.shortcuts import render
from .models import CustomUser
from rest_framework import generics #提供常見的視圖類別，如C、R、U、D 
from .serializers import UserSerializer #用於將資料轉換JSON或模型的格式
from .permissions import ( #自定義的身份驗證
    IsWarehouseUser,
    IsSaleUser,
)
# DRF內置的API驗證，管理API能被哪些人訪問
# IsAuthenticated：只有經過身份驗證的用戶才能訪問，被拒絕則收到401；AllowAny能讓任何人訪問特定的API，無論用戶是否經過身份驗證
from rest_framework.permissions import AllowAny, IsAuthenticated
import logging #載入偵錯模組

logger = logging.getLogger("api")

# Create your views here.

class CreateUserView(generics.CreateAPIView):
    """
    建立新使用者的API
    """
    #查詢所有CustomUser模型實例，用於指定查詢的對象
    queryset = CustomUser.objects.all()
    #處理CustomUser模型的資料轉換與驗證資料是否存在與格式正確，成功後會建立新的使用者，失敗則返回400 
    serializer_class = UserSerializer 
    permission_classes = [AllowAny] #任何人都可以註冊


from django.http import JsonResponse

def test_error(request):
    raise ValueError("這是一個測試錯誤")

def my_view(request):
    try:
        result = 1 / 0  # 這裡會發生錯誤
    except Exception as e:
        logger.error("發生錯誤: %s", str(e))  # 記錄錯誤，寫入 logs/errors.log
