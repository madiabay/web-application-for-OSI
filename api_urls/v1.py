from django.urls import path, include


urlpatterns = [
    path('', include('house_services.urls.v1')),
]