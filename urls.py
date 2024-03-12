from .views import UserViewSet,MembershipViewSet,CategoryViewSet,ServiceViewSet,AppointmentViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
#register your views
router.register('user', UserViewSet, basename='user')
router.register('membership', MembershipViewSet, basename='membership')
router.register('service', ServiceViewSet, basename='service')
router.register('category', CategoryViewSet, basename='category')
router.register('appointment', AppointmentViewSet, basename='appointment')

urlpatterns =  router.urls
