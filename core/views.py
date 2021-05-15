from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import redirect, render, reverse
from django.views.generic.edit import FormView

from core.forms import RegisterForm, UserLoginForm


def home(request):
    print(request.user)
    return render(request, 'core/home.html')


class doLoginView(FormView):
    success_url = "/"
    form_class = UserLoginForm
    template_name = "Login.html"

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            login(request, form.cleaned_data.get('user_obj'))
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


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
