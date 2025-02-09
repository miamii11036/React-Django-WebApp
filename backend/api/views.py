from django.shortcuts import render
# from .models import CustomUser, Memo
from rest_framework import generics #提供常見的視圖類別，如C、R、U、D 
# from .serializers import (
#     # UserSerializer, 
#     # MemoSerializer #用於將資料轉換JSON或模型的格式
# )
# from .permissions import ( #自定義的身份驗證
#     # IsWarehouseUser,
#     # IsSaleUser,
# )
# DRF內置的API驗證，管理API能被哪些人訪問
# IsAuthenticated：只有經過身份驗證的用戶才能訪問，被拒絕則收到401；AllowAny能讓任何人訪問特定的API，無論用戶是否經過身份驗證
from rest_framework.permissions import AllowAny
import logging #載入偵錯模組

logger = logging.getLogger("api")

# Create your views here.

# class MemoListCreate(generics.ListCreateAPIView):
#     """
#     顯示當下使用者的所有備忘錄，並提供新增備忘錄的API
#     """
#     permission_classes = [IsWarehouseUser, IsSaleUser] #只有Warehouse或Sale的使用者可以訪問
#     serializer_class = MemoSerializer

#     def get_queryset(self):
#         """
#         取得當下使用者的所有備忘錄
#         """
#         user = self.request.user
#         return Memo.objects.filter(author=user)

# class CreateUserView(generics.CreateAPIView):
#     """
#     建立新使用者的API
#     """
#     #查詢所有CustomUser模型實例，用於指定查詢的對象
#     queryset = CustomUser.objects.all()
#     #處理CustomUser模型的資料轉換與驗證資料是否存在與格式正確，成功後會建立新的使用者，失敗則返回400 
#     serializer_class = UserSerializer 
#     permission_classes = [AllowAny] #任何人都可以註冊