from rest_framework.serializers import ModelSerializer

from auth_app.models import Posts


class PostSerializer(ModelSerializer):

    class Meta:
        model = Posts
        fields = ('name', 'description', 'is_public')
