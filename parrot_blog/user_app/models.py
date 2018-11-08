from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser


class BlogUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars', blank=True)

    def groups_to_str(self):
        groups = self.groups.all()
        result = ','.join([item.name for item in groups])
        return result