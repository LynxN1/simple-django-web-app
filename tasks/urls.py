from django.urls import path

from .views import Tasks, CreateTaskView

urlpatterns = [
    path('', Tasks.as_view(), name='tasks'),
    path('create/', CreateTaskView.as_view(), name='create_task')
]
