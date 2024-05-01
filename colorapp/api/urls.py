from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

router = routers.DefaultRouter()
router.register(r'palettes', views.PaletteViewSet, basename='palette')
router.register(r'colors', views.ColorViewSet, basename='color')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("users/", views.UsersApi.as_view(), name="users_api"),
]

urlpatterns += router.urls
