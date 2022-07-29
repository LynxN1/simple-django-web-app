from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, TemplateView
from django.shortcuts import redirect, render
from django.views.generic import CreateView

from profile.forms import LoginForm, RegisterForm


class Login(LoginView):
    form_class = LoginForm
    template_name = 'profile/login.html'
    redirect_authenticated_user = True


class Logout(LogoutView):
    next_page = 'login'


class Register(CreateView):
    template_name = 'profile/register.html'
    form_class = RegisterForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to='login')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created successfully')
            return redirect(to='login')
        return render(request, self.template_name, {'form': form})


class Profile(LoginRequiredMixin, TemplateView):
    template_name = 'profile/index.html'
