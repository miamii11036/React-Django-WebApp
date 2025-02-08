from rest_framework.permissions import (
    BasePermission, # 使用DRF提供的BasePermission讓使用者擴展權限類別，控制哪些用戶可以訪問或操作API
)
from .models import UserRole
import logging #偵錯

logger = logging.getLogger("api")

class IsWarehouseUser(BasePermission):
    """
    檢查該使用者是否通過JWT驗證且身份(role)是否為Warehouse
    1. 繼承BasePermission權限控制類別
    2. 使用has_permission進行權限檢查，當API被請求時，系統會自動檢查該使用者身份是否允許訪問view
    """

    def has_permission(self, request, view):
        # request.user.is_authenticated確保使用者通過JWT驗證
        # request.user.role == UserRole.WAREHOUSE 檢查使用者的role是否為Warehouse
        return request.user.is_authenticated and request.user.role == UserRole.WAREHOUSE


class IsSaleUser(BasePermission):
    """
    檢查該使用者是否通過JWT驗證且身份(role)是否為Sale
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == UserRole.SALE
