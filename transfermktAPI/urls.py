from django.urls import path,include
from .views import index,TransferAPI,latest
from rest_framework import routers

router = routers.DefaultRouter()
router.register("transfers",TransferAPI)

urlpatterns = [
    path('', index , name = 'index'),
    path('', include(router.urls)),
    path('latest', latest , name = 'latest'),
]