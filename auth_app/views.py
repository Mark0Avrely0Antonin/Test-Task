from rest_framework.generics import ListAPIView

from auth_app.serializers import PostSerializer
from auth_app.models import Posts
from auth_app.permissions import CustomPermission


class ListPosts(ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = (CustomPermission, )

