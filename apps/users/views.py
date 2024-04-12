from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView, View, ListView, UpdateView, CreateView, TemplateView

from .models import (
    User
)
from .forms import (
    LoginForm,
    ModifyUserForm,
    ResetPasswordForm,
    RegisterUserForm
)


class Login(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('dashboard:dashboard')

    def form_valid(self, form):
        message = ""
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user is None:
            message = "The user does not exist or the password is incorrect"
        else:
            login(self.request, user)

            next_url = self.request.GET.get("next", None)
            self.success_url = self.success_url if next_url is None else next_url

            messages.success(self.request, "Session started successfully")
            return super(Login, self).form_valid(form)

        form.add_error('username', message)
        form.add_error('password', message)
        messages.error(self.request, message)
        return super(Login, self).form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Enter a valid username and password to access the system")
        return super(Login, self).form_invalid(form)


class Logout(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, "Session closed successfully")
        return redirect('login')


class UsersList(LoginRequiredMixin, ListView):
    model = User
    context_object_name = "users"
    template_name = "users/user_list.html"

    def get_queryset(self):
        return User.objects.all().exclude(username="admin")


class ModifyUser(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ModifyUserForm
    template_name = 'users/modify.html'
    success_url = reverse_lazy('users:user_list')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.username = user.email
        user.save()
        return super().form_valid(form)


class ResetPassword(LoginRequiredMixin, FormView):
    form_class = ResetPasswordForm
    template_name = "users/reset_password.html"
    success_url = reverse_lazy('users:user_list')

    def get_context_data(self, *args, **kwargs):
        context = super(ResetPassword, self).get_context_data(**kwargs)
        context['user'] = get_object_or_404(User, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        password = form.cleaned_data['password1']
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        user.set_password(password)
        user.save()
        return super(ResetPassword, self).form_valid(form)

class Deactivate(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = get_object_or_404(User, pk=user_id, is_active=True)
        user.is_active = False
        user.save()
        messages.success(request, "The user has been deactivated successfully")
        return redirect('users:user_list')

class Activate(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = get_object_or_404(User, pk=user_id, is_active=False)
        user.is_active = True
        user.save()
        messages.success(request, "The user has been activated successfully")
        return redirect('users:user_list')


class Register(LoginRequiredMixin, CreateView):
    model = User
    form_class = RegisterUserForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:register")

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password1']

        user = form.save(commit=False)
        user.username = email
        user.save()

        user.set_password(password)

        return super().form_valid(form)