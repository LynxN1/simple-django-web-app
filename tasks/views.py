from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView

from tasks.models import Task


class Tasks(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = context['object_list'].filter(author=self.request.user)
        return context


def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(title=title, author=request.user)
        return redirect('tasks')
    if request.method == 'GET':
        return redirect('tasks')


# class CreateTaskView(CreateView):
#     model = Task
#     template_name = 'tasks/create_task_modal.html'
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super(CreateTaskView, self).form_valid(form)
