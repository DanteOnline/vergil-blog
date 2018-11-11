from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, HttpResponseRedirect, Http404
from django.contrib import auth, messages
from django.conf import settings
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, FormView

from main_app.views import random_picture
from user_app.models import BlogUser
from .forms import BlogUserRegistrationForm, BlogUserAuthenticationForm


class LoginFormView(SuccessMessageMixin, FormView):
    form_class = BlogUserAuthenticationForm
    template_name = 'auth.html'
    success_url = '/'
    success_message = 'Добро пожаловать'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context[settings.PAGE_HEADER] = 'Авторизация'
        # context[settings.PAGE_SUBHEADER] = 'Для входа на сайт введите свой логин и пароль'
        context.update({
            settings.PAGE_HEADER: 'Авторизация',
            settings.PAGE_SUBHEADER: 'Для входа на сайт введите свой логин и пароль'
        })
        return context

    def form_valid(self, form):
        current_user = form.get_user()
        auth.login(self.request, current_user)
        return super().form_valid(form)


def logout(request):
    # TODO: В шаблоне через форму едет верстка, сделать метод пост и переделать верстку
    # if request.method == 'POST':
    #     auth.logout(request)
    #     return HttpResponseRedirect(reverse('users:login'))
    # else:
    #     raise Http404
    auth.logout(request)
    messages.add_message(request, messages.SUCCESS, 'Пока')
    return HttpResponseRedirect(reverse('users:login'))


# Попробуем через createview сделать регистрацию
class BlogUserCreateView(SuccessMessageMixin, CreateView):
    # model = BlogUser
    success_url = reverse_lazy('users:login')
    success_message = 'Вы успешно зарегистрировались'
    template_name = 'registration.html'
    form_class = BlogUserRegistrationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({
            settings.PAGE_HEADER: 'Регистрация',
            settings.PAGE_SUBHEADER: 'Присоединяйтесь. Будем знакомы',
            settings.PAGE_IMAGE_URL: random_picture(['violet.jpg', 'blue.jpg'])
        })
        return context
