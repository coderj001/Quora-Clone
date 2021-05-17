from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormMixin

from core.forms import UserProfileForm
from core.models import User


@login_required(login_url=reverse_lazy("core:login-view"))
def home(request):
    print(request.user)
    return render(request, 'core/home.html')


class UserProfile(SingleObjectMixin, FormMixin, View):
    # for SingleObjectMixin
    model = User
    queryset = User.objects.all()

    # for FormMixin
    form_class = UserProfileForm

    template_name = "core/profile.html"

    def get_initial(self):
        instant = self.get_object()
        return {
            'email': instant.email,
            'first_name': instant.first_name,
            'last_name': instant.last_name,
            'bio': instant.bio,
        }

    def get_context_data(self, **kwargs):
        """Insert the single object into the context dict."""
        context = {}
        if self.object:
            context['object'] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object

        """Insert the form into the context dict."""
        if self.request.user.id == self.get_object().id:
            if 'form' not in kwargs:
                kwargs['form'] = self.get_form()

        context.update(kwargs)
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return render(request, self.template_name, context=context)
