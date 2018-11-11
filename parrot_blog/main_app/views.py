from random import choice
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.http import Http404
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q


from .models import Post
from .forms import PostForm


def random_picture(pictures):
    # pictures = [
    #     'black.jpg',
    #     'violet.jpg',
    #     'blue.jpg'
    # ]

    r_image = choice(pictures)
    url = '/static/img/backgrounds/{}'.format(r_image)
    return url


class PostListView(ListView):
    model = Post
    template_name = 'list.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[settings.PAGE_HEADER] = 'Попчанская жизнь'
        context[settings.PAGE_SUBHEADER] = 'Блог волнистика Вергилия'
        # context[settings.PAGE_IMAGE_URL] = '/static/img/backgrounds/all_parrots.jpg/'
        # context[settings.PAGE_IMAGE_URL] = '/static/img/backgrounds/all_parrots_black.jpg/'
        # context[settings.PAGE_IMAGE_URL] = '/static/img/backgrounds/vergil.jpg/'
        #context[settings.PAGE_IMAGE_URL] = '/static/img/backgrounds/cockatoo_pink.jpg/'
        context[settings.PAGE_IMAGE_URL] = random_picture(['violet.jpg', 'blue.jpg'])

        return context

    def get_queryset(self):
        return Post.objects.filter(is_active=True)
        # кому то выводим все
        # if self.request.user.has_perm('main_app.moderate_post'):
        #     return Post.objects.all()
        # else:
        #     return Post.objects.filter(is_active=True)
            # Выводим активные или этого автора
            # return Post.objects.filter(Q(is_active=True) | Q(user=self.request.user))


class PostAutorListView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'

    def get(self, request, *args, **kwargs):
        author_id = kwargs.get('author_id')
        self.author_id = author_id
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        posts = Post.objects.filter(user__id=self.author_id)
        if self.request.user.is_superuser:
            return posts
        else:
            return posts.filter(is_active=True)


@method_decorator(permission_required('main_app.create_post'), name='dispatch')
class PostCreateView(SuccessMessageMixin, CreateView):
    model = Post
    template_name = 'create.html'
    success_url = '/'
    form_class = PostForm
    success_message = 'Твой пост был создан и отправлен на модерацию'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[settings.PAGE_HEADER] = 'Добавить пост'
        context[settings.PAGE_SUBHEADER] = 'Просто заполни поля ниже'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(permission_required('main_app.edit_post'), name='dispatch')
class PostUpdateView(SuccessMessageMixin, UpdateView):
    model = Post
    template_name = 'create.html'
    success_url = '/'
    form_class = PostForm
    success_message = 'Твой пост был отредактирован и отправлен на модерацию'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[settings.PAGE_HEADER] = 'Редактировать пост'
        context[settings.PAGE_SUBHEADER] = 'Просто заполни поля ниже'
        return context

    # TODO: После редактирования надо снова ставить пост на модерацию если это не админ создал


@method_decorator(permission_required('main_app.drop_post'), name='dispatch')
class PostDeleteView(SuccessMessageMixin, DeleteView):
    model = Post
    template_name = 'delete_confirm.html'
    success_url = '/'
    context_object_name = 'post'
    success_message = 'Пост был успешно удален'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = context['post']
        context[settings.PAGE_HEADER] = 'Вы действительно хотите удалить {} ?'.format(post.title)
        context[settings.PAGE_SUBHEADER] = post.subtitle
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


class PostDetailView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.backgroud_picture = random_picture(['violet.jpg', 'blue.jpg'])
        if obj.is_active:
            return obj
        else:
            raise Http404
