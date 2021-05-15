from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render, reverse
from django.views.generic.edit import FormView

from core.forms import UserCreationForm, UserLoginForm


def home(request):
    print(request.user)
    return render(request, 'core/home.html')


class doLoginView(FormView):
    success_url = '/'
    form_class = UserLoginForm
    template_name = "Login.html"

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            user = form.cleaned_data.get('user_obj')
            login(request, user)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class RegisterView(FormView):
    success_url = '/'
    form_class = UserCreationForm
    template_name = "Register.html"

    def post(self, request):
        form = self.get_form()
        if form.is_valid():
            instant = form.save()
            instant.save()
            login(request, instant)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


def user_logout(request):
    logout(request)
    return redirect(reverse("core:login-view"))
