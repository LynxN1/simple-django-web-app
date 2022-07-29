from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class Tasks(LoginRequiredMixin, TemplateView):
    template_name = 'tasks/index.html'
