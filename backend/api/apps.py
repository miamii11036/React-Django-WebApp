from django.apps import AppConfig
import logging #偵錯

logger = logging.getLogger("api")

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
