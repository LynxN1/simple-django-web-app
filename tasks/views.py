from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from tasks.forms import TaskForm
from tasks.models import Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = context['object_list'].filter(author=self.request.user).order_by('-created_at')
        return context


class CreateTaskView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'tasks/modals/create_task_modal.html'
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


class DeleteTaskView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
    template_name = 'tasks/modals/delete_task_modal.html'

    def get(self, request, *args, **kwargs):
        if not is_ajax(request):
            return redirect('tasks')
        return super().get(request, *args, **kwargs)


class UpdateTaskView(LoginRequiredMixin, UpdateView):
    model = Task
    success_url = reverse_lazy('tasks')
    template_name = 'tasks/modals/update_task_modal.html'
    form_class = TaskForm

    def get(self, request, *args, **kwargs):
        if not is_ajax(request):
            return redirect('tasks')
        return super().get(request, *args, **kwargs)


def is_ajax(request):
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'
