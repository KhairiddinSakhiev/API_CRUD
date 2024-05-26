from django.urls import path
from .views import DataListCreateView


from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("", DataListCreateView, basename="Data")

urlpatterns = router.urls