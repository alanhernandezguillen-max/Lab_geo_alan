from django.urls import path, include
from .routers import router

urlpatterns = [
    path('api-alan/', include(router.urls))
]