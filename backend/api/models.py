from django.db import models
# from django.contrib.auth.models import (
#     # AbstractUser,  ##用於擴展Django內建的User model欄位
# ) 
import logging #偵錯

logger = logging.getLogger("api")
# Create your models here.


# class UserRole(models.TextChoices):
#     """
#     設定註冊者能夠選擇的role(職位)的選項
#     """

#     WAREHOUSE = "Warehouse"
#     SALE = "Sale"


# class CustomUser(AbstractUser):
#     """
#     將UserRole作為新欄位新增至Django預設的User model (管理與使用者認證相關的功能)
#     註冊時，使用者目前只能選擇Warehouse或Sale，且預設選項為Warehouse
#    _ """

#     role = models.CharField(
#         max_length=20,
#         choices=UserRole.choices,  ##設定role欄位的選項
#         default=UserRole.WAREHOUSE,  ##role欄位的預設選項
#     )
#     ###將預設的User model擴展成有role欄位的CustomUser，所以要在setting.py將預設指定為新model

# class Memo(models.Model):
#     """
#     用於儲存使用者的備忘錄，儲存標題、內容、建立時間、通知時間
#     """

#     author = models.ForeignKey(
#         CustomUser,  ##使用者的外鍵
#         on_delete=models.CASCADE,  ##當使用者被刪除時，將其關聯的備忘錄一併刪除
#         related_name="memos",  ##設定反向查詢的名稱
#     )
#     title = models.CharField(max_length=100)  ##標題
#     content = models.TextField()  ##內容
#     created_at = models.DateTimeField(auto_now_add=True)  ##建立時間
#     notified_at = models.DateTimeField(null=True, blank=True)  ##通知時間

#     def __str__(self):
#         return self.title  ##顯示標題