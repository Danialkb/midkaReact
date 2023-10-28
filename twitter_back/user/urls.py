from rest_framework.routers import DefaultRouter

from post.views import PostViewSet
from user.views import UserView

router = DefaultRouter()

router.register(r"", UserView)

urlpatterns = router.urls
