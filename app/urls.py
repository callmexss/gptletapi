from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AppViewSet,
    OpenAIView,
    GPTEntryViewSet,
    URLProcessView,
)


router = DefaultRouter()
router.register(r"apps", AppViewSet)
router.register(r"gpts", GPTEntryViewSet)

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/openai/", OpenAIView.as_view(), name="openai"),
    path('v1/process_url/', URLProcessView.as_view(), name='process-url'),
]
