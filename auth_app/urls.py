from django.urls import path

from auth_app.views import ListPosts

urlpatterns = [
    path('list_posts/', ListPosts.as_view(), name='list_posts'),
]
