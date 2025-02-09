from django.db import models
from django.contrib.auth.models import (
    User,  ##Django的預設User模型，管理與使用者認證相關的功能，提供基本欄位，如用戶名、密碼、電郵、群組與權限
) 
import logging #偵錯

logger = logging.getLogger("api")
# Create your models here.

class Memo(models.Model):
    """
    用於儲存使用者的備忘錄，儲存標題、內容、建立時間、通知時間
    """

    author = models.ForeignKey(
        User,  ##使用者的外鍵
        on_delete=models.CASCADE,  ##當使用者被刪除時，將其關聯的備忘錄一併刪除
        related_name="memos",  ##設定反向查詢的名稱
    )
    title = models.CharField(max_length=100)  ##標題
    content = models.TextField()  ##內容
    created_at = models.DateTimeField(auto_now_add=True)  ##建立時間
    notified_at = models.DateTimeField(null=True, blank=True)  ##通知時間

    def __str__(self):
        return self.title  ##顯示標題