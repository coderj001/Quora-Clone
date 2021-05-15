from django.contrib.auth import login, logout
from django.shortcuts import redirect, render, reverse
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required

from core.forms import UserCreationForm, UserLoginForm


class doLoginView(FormView):
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

    def get_success_url(self):
        next_url = self.request.GET.get('next', None)
        if next_url:
            return str(next_url)
        else:
            return reverse('core:home')


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


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse("core:login-view"))
