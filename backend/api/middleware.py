import logging #偵錯
from django.http import JsonResponse

logger = logging.getLogger("api")

class ErrorLoggingMiddleware:
    """ 捕捉未處理的例外，記錄錯誤日誌，並回應 JSON """

    def __init__(self, get_response):
        self.get_response = get_response 

    def __call__(self, request):
        try:
            response = self.get_response(request) #獲取HTTP響應
            return response
        except Exception as e:
            logger.error("未處理的例外: %s", str(e), exc_info=True) 
            #exc_info=True 會記錄完整 traceback
            return JsonResponse({"error": "發生內部錯誤"}, status=500)