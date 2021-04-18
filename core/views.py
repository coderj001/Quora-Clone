from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render, reverse
from django.views.generic.edit import FormView

from django.http import HttpResponse
from core.forms import RegisterForm


def home(request):
    return HttpResponse('<h1>Home</h1>')


class RegisterView(FormView):
    success_url = '/'

    def get(self, request):
        content = {}
        content['form'] = RegisterForm
        return render(request, 'register.html', content)

    def post(self, request):
        content = {}
        form = RegisterForm(request.POST, request.FILES or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect(reverse('dashboard-view'))
        content['form'] = form
        template = 'register.html'
        return render(request, template, content)
