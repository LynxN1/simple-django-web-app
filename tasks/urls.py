from django.urls import path

from .views import Tasks, create_task

urlpatterns = [
    path('', Tasks.as_view(), name='tasks'),
    path('create/', create_task, name='create_task')
]
