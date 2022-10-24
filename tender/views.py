from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Tab

from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect

from .forms import UserCreationForm


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
import datetime
def Index(request):
    tabs = Tab.objects.filter(is_active=False).order_by('data2')
    context = {'tabs': tabs,'now': datetime.datetime.now()}
    return render(request, 'home.html', context)

def Index_Cit(request):
    tabs = Tab.objects.filter(is_active=False, staffer__name__istartswith='Ситник').order_by('data2')
    context = {'tabs': tabs}
    return render(request, 'cit.html', context)

def Index_Kal(request):
    tabs = Tab.objects.filter(is_active=False, staffer__name__istartswith='Кальницкий').order_by('data2')
    context = {'tabs': tabs}
    return render(request, 'kal.html', context)

def Index_Mur(request):
    tabs = Tab.objects.filter(is_active=False, staffer__name__istartswith='Муромцева').order_by('data2')
    context = {'tabs': tabs}
    return render(request, 'mur.html', context)

def Index_Skor(request):
    tabs = Tab.objects.filter(is_active=False, staffer__name__istartswith='Скоробогатая').order_by('data2')
    context = {'tabs': tabs}
    return render(request, 'skor.html', context)

def Index_Mir(request):
    tabs = Tab.objects.filter(is_active=False, staffer__name__istartswith='Мирончик').order_by('data2')
    context = {'tabs': tabs}
    return render(request, 'mir.html', context)

def Index_Evt(request):
    tabs = Tab.objects.filter(is_active=False, staffer__name__istartswith='Евтеев').order_by('data2')
    context = {'tabs': tabs}
    return render(request, 'evt.html', context)