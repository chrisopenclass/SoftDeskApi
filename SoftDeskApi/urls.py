from django.contrib import admin
from django.urls import path,  include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', include('project.urls')),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
