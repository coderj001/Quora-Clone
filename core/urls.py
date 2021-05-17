from django.urls import path

from core.adminviews import AdminDashBoard
from core.authviews import RegisterView, doLoginView, user_logout
from core.views import home, UserProfile

app_name = 'core'

urlpatterns = [
    # core views
    path('', home, name='home'),
    path('p/<uuid:pk>/', UserProfile.as_view(), name='profile'),

    # Auth views
    path('register/', RegisterView.as_view(), name='register-view'),
    path('login/', doLoginView.as_view(), name="login-view"),
    path('logout/', user_logout, name="logout"),

    # Dashborad
    path('dashboard/', AdminDashBoard.as_view(), name="dashboard"),
]
