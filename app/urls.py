from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppViewSet, OpenAIView


router = DefaultRouter()
router.register(r"apps", AppViewSet)

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/openai/", OpenAIView.as_view(), name="openai"),
]
