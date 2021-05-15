from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class LoginMiddleware(MiddlewareMixin):

    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        # print(modulename)
        user = None
        if modulename == 'core.authviews' or modulename == 'django.views.static':
            pass
        else:
            user = request.user
            if user.is_authenticated:
                if not user.is_admin:
                    if modulename == 'core.adminviews':
                        return HttpResponseRedirect(reverse('core:home'))
                else:
                    pass
