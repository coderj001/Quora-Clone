from core.views import RegisterView, home
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('register/', RegisterView.as_view(), name='register-view'),
]
