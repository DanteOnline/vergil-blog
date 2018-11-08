
from django.conf.urls import url
from django.contrib import admin
from main_app.views import PostDetailView, PostAutorListView
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^(?P<author_id>\d+)/$', PostAutorListView.as_view(), name='by_author'),
    path('about/', include('about_app.urls', namespace='about')),
    path('', include('main_app.urls', namespace='posts')),
    path('users/', include('user_app.urls', namespace='users')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
