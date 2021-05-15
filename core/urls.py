from django.urls import path

from core.views import RegisterView, doLoginView, home, user_logout
from core.adminviews import AdminDashBoard

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('register/', RegisterView.as_view(), name='register-view'),
    path('login/', doLoginView.as_view(), name="login-view"),
    path('logout/', user_logout, name="logout"),

    # Dashborad
    path('dashboard/', AdminDashBoard.as_view(), name="dashboard"),
]
