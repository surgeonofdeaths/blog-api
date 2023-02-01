from .views import PostViewSet, UserViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(prefix='', viewset=PostViewSet, basename='posts')
router.register('users', UserViewSet, basename='users')
urlpatterns = router.urls
