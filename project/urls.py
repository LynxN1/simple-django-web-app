from django.contrib import admin
from django.urls import path, include

from mainpage.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('tasks/', include('tasks.urls')),
    path('profile/', include('profile.urls')),
]
