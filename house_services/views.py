from django.shortcuts import render, redirect

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
from users.models import CustomUser

from django.views.generic import CreateView
from django.http import JsonResponse
from django.views import View

import requests


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


# #test
# def my_view(request):
#     # Retrieve data from endpoint
#     response = requests.get('http://my-endpoint.com/data')
#     data = response.json()

#     # Pre-fill form field with data from endpoint
#     initial_data = {'my_field': data['my_data']}
#     form = MyForm(initial=initial_data)

#     return render(request, 'my_template.html', {'form': form})
# #test



def addnots(request, user_id):
    initial_data = {'author': CustomUser.objects.get(pk=user_id)}
    print(initial_data)
    if request.method == 'POST':
        # response = requests.get(str(request.path))
        # print(response)
        # data = response.json()
        # print(data)
        form = forms.NotificationForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                models.House_service.objects.create(**form.cleaned_data, **initial_data)
                return redirect(to='home')
            except:
                form.add_error(None, 'Ошибка добавления поста')

            # form.save()
            return redirect(to='home')
    else:
        form = forms.NotificationForm()


    return render(request,
                  'house_services/add_nots.html',
                  {'form': form, 'user_id': user_id}
                  )

def getUsers(request):
    queryset = models.House_service.objects.all()

    return JsonResponse({'nots': list(queryset.values())})


# class AddNotification(CreateView):
#     form_class = forms.NotificationForm()
#     template_name = 'house_services/add_nots.html'
#     success_url = reverse_lazy('add_nots')

#     # def get(self, request, *args, **kwargs):
#     #     if request.user.is_authenticated:
#     #         user_id = request.user.id
#     #         return redirect(f'/user/{user_id}/')
#     #     else:
#     #         # handle unauthenticated users
    

#     def getUsers(request):
#         queryset = models.House_service.objects.all()

#         return JsonResponse({'nots': list(queryset.values())})


# def getUsers(request):
#     queryset = models.House_service.objects.all()

#     return JsonResponse({'nots': list(queryset.values())})

class MyView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user_id = request.user.id
            return redirect(f'/api/v1/add_nots/{user_id}/')
        else:
            return redirect('login')