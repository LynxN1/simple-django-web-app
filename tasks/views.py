from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView

from tasks.forms import TaskForm
from tasks.models import Task


class Tasks(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = context['object_list'].filter(author=self.request.user).order_by('-created_at')
        return context


class CreateTaskView(CreateView):
    model = Task
    template_name = 'tasks/create_task_modal.html'
    form_class = TaskForm

    def get(self, request, *args, **kwargs):
        if not is_ajax(request):
            return redirect('tasks')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.author = request.user
            form_instance.save()
            return redirect('tasks')
        return render(request, self.template_name, {'form': form})


def is_ajax(request):
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'
