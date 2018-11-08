from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings


# Create your views here.
class AboutTemplateView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[settings.PAGE_HEADER] = 'О сайте'
        context[settings.PAGE_SUBHEADER] = 'Пишите посты на свою любимую тему вместе с нами'
        return context
