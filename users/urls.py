from .views import UserViewSet
from django.urls import path

urlpatterns = [
    path('signup/', UserViewSet.as_view()),
]
