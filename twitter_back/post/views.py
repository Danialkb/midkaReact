from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from post.models import *
from post.serializers import *


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    search_fields = ["^title"]

    @action(detail=True, methods=["POST"])
    def like(self, request, *args, **kwargs):
        id = kwargs.get("pk")

        post = Post.objects.get(id=id)

        post.likes += 1
        post.save()
        return Response({"ok": "ok"}, status=200)
