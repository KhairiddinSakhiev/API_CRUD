from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
path('', views.getData, name="datas"),
path('post/', views.postData, name="create_datas"),
path('update/<int:pk>/', views.updateData, name="update_datas"),
path('delete/<int:pk>/', views.deleteData, name="delete_datas"),
]