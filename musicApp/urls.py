from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from .views import MainPageView, upload
from .api import QueryWorksViewSet

app_name = 'musicApp'
router = routers.DefaultRouter()
router.register(r'worklist', QueryWorksViewSet,basename='worklist-list')

urlpatterns = [
    path('', MainPageView.as_view(), name='mainpage'),
    path('upload/', upload, name="upload"),
    path('api/', include(router.urls)),
]
