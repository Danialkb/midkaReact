from rest_framework.serializers import ModelSerializer
from post.models import *


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ("image", )


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

