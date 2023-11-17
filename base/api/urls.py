from django.urls import path
from . import views
from .views import MyTokenObtainPairView
from base.api.viewsets import ClientViewSet
from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


router = routers.DefaultRouter()
router.register('client',ClientViewSet)

urlpatterns = [
    path('',views.getRoutes),
    path('notes/',views.getNotes),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls  #combine both vies and viewset in a single url pattern
