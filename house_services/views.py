from django.shortcuts import render

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

from . import forms, models

from django.views.generic import CreateView
from django.http import JsonResponse


class RegisterUser(CreateView):
    form_class = forms.UserCreationFormmm
    template_name = 'house_services/register.html'
    success_url = reverse_lazy('login')

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'house_services/login.html'

#########################

menu = ['About site', 'Add Nots', 'Feedback', 'Login']
def index(request):
    context = {
        'menu': menu
    }
    return render(request, 'house_services/index.html', context)

class AddNotification(CreateView):
    form_class = forms.NotificationForm
    template_name = 'house_services/add_nots.html'
    success_url = reverse_lazy('add_nots')


def getUsers(request):
    queryset = models.House_service.objects.all()

    return JsonResponse({'nots': list(queryset.values())})