from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ImageSpecField
from imagekit.processors import *


# Create your models here.
class Post(models.Model):
    class Meta:
        ordering = ['-post_datetime']
        permissions = (
            ("create_post", "Может создать пост"),
            ("edit_post", "Может изменить пост"),
            ("drop_post", "Может удалить пост"),
            ("moderate_post", "Может модерировать пост"),
        )

    title = models.CharField(max_length=64, unique=True)
    subtitle = models.CharField(max_length=128, blank=True)
    post_datetime = models.DateTimeField(auto_now=True)
    # Текст для показа в списке
    preview_text = models.CharField(max_length=200, verbose_name='Текст для превью')
    text = RichTextUploadingField(config_name='default')
    is_active = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='posts', verbose_name='Основное изображение')
    video_code_url = models.URLField(blank=True)

    post_thumb = ImageSpecField(source='image',
                                processors=[ResizeToFit(1000, 500, upscale=True),
                                            Adjust(color=1, brightness=1, contrast=1.0, sharpness=1.0)],

                                format='JPEG',
                                options={'quality': 100})

    image_thumbnail = ImageSpecField(source='image',

                                     processors=[ResizeToFit(300, 300)],

                                     format='JPEG',
                                     options={'quality': 100})

    # TODO: добавить галерею и ссылку на видео

    def first_text(self):
        text = self.text
        return text[:20]

    def __str__(self):
        return self.title
