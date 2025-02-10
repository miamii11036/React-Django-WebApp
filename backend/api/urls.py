from django.urls import path
from . import views

urlpatterns = [
    path("memos/", views.MemoListCreate.as_view(), name="memo-list-create"),
    path("memos/delete/<int:pk>", views.MemoDelete.as_view(), name="memo-delete"), 
]