from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, reverse
from django.views import View


class AdminDashBoard(LoginRequiredMixin, View):
    template_name = 'admin/Dashboard.html'
    login_url = '/login'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context=context)
