# from rest_framework.routers import DefaultRouter

# from house_services import views


# router = DefaultRouter()
# router.register(r'house_service-images', views.House_serviceImageViewSet)
# router.register(r'house_service', views.House_serviceViewSet)

# urlpatterns = router.urls

####################################################################################################

from django.views.decorators.cache import cache_page

from django.urls import path
from house_services import views


urlpatterns = [
    path('register/', views.RegisterUser.as_view(), name='register'),
]