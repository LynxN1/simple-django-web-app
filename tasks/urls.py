from django.urls import path

from .views import TaskListView, CreateTaskView, DeleteTaskView, UpdateTaskView

urlpatterns = [
    path('', TaskListView.as_view(), name='tasks'),
    path('create/', CreateTaskView.as_view(), name='create_task'),
    path('delete/<int:pk>', DeleteTaskView.as_view(), name='delete_task'),
    path('update/<int:pk>', UpdateTaskView.as_view(), name='update_task'),
]
