from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import View


@login_required(login_url=reverse_lazy("core:login-view"))
def home(request):
    print(request.user)
    return render(request, 'core/home.html')


class UserProfile(View):
    pass
