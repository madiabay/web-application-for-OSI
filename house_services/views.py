from rest_framework.viewsets import ModelViewSet

from . import serializers, models


class House_serviceImageViewSet(ModelViewSet):
    serializer_class = serializers.House_serviceImageSerializer
    queryset = models.House_serviceImage.objects.all()


class House_serviceViewSet(ModelViewSet):
    serializer_class = serializers.House_serviceSerializer
    queryset = models.House_service.objects.all()

###################################################################################################

from django.views.generic import ListView, DetailView, CreateView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

from . import forms


class RegisterUser(CreateView):
    form_class = forms.UserCreationFormmm
    template_name = 'house_services/register.html'
    success_url = reverse_lazy('login')

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'house_services/login.html'