from django.contrib import admin
from .models import BlogUser


class BlogUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_superuser', 'groups_to_str']
# Register your models here.
admin.site.register(BlogUser, BlogUserAdmin)