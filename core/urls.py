from core.views import RegisterView, home, doLoginView
from django.urls import path

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('register/', RegisterView.as_view(), name='register-view'),
    path('login/', doLoginView.as_view(), name="login-view"),
]
