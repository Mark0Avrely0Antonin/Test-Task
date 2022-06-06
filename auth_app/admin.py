from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from auth_app.models import CustomUser, Posts


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_public')
    list_filter = ('is_public',)
    search_fields = ('name', 'is_public')


admin.site.register(CustomUser)