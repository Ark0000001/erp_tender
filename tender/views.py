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
    context = {'tabs': tabs,'now': datetime.datetime.now()}
    return render(request, 'cit.html', context)

def Index_Kal(request):
    tabs = Tab.objects.filter(is_active=False, staffer__name__istartswith='Кальницкий').order_by('data2')
    context = {'tabs': tabs,'now': datetime.datetime.now()}
    return render(request, 'kal.html', context)

def Index_Mur(request):
    tabs = Tab.objects.filter(is_active=False, staffer__name__istartswith='Муромцева').order_by('data2')
    context = {'tabs': tabs,'now': datetime.datetime.now()}
    return render(request, 'mur.html', context)

def Index_Skor(request):
    tabs = Tab.objects.filter(is_active=False, staffer__name__istartswith='Скоробогатая').order_by('data2')
    context = {'tabs': tabs,'now': datetime.datetime.now()}
    return render(request, 'skor.html', context)

def Index_Mir(request):
    tabs = Tab.objects.filter(is_active=False, staffer__name__istartswith='Мирончик').order_by('data2')
    context = {'tabs': tabs,'now': datetime.datetime.now()}
    return render(request, 'mir.html', context)

def Index_Evt(request):
    tabs = Tab.objects.filter(is_active=False, staffer__name__istartswith='Евтеев').order_by('data2')
    context = {'tabs': tabs,'now': datetime.datetime.now()}
    return render(request, 'evt.html', context)


def addition(request):

    num1 = request.POST['num1']
    num2 = request.POST['num2']

    if num1.isdigit() and num2.isdigit():
        a = int(num1)
        b = int(num2)
        p=a-b
        res = p/a*100

        return render(request, "result.html", {"result": res})
    else:
        res = "Не корректно введены данные"
        return render(request, "result.html", {"result": res})

def pri(request):

    num1 = request.POST['num1']
    num2 = request.POST['num2']

    if num1.isdigit() and num2.isdigit():
        a = int(num1)
        b = int(num2)
        p=a*b/100
        res = p

        return render(request, "result.html", {"result": res})
    else:
        res = "Не корректно введены данные"
        return render(request, "result.html", {"result": res})

def seb(request):

    num1 = request.POST['num1']
    num2 = request.POST['num2']

    if num1.isdigit() and num2.isdigit():
        a = int(num1)
        b = int(num2)
        p=a*b/100
        res = b-p

        return render(request, "result.html", {"result": res})
    else:
        res = "Не корректно введены данные"
        return render(request, "result.html", {"result": res})

def vyr(request):

    num1 = request.POST['num1']
    num2 = request.POST['num2']

    if num1.isdigit() and num2.isdigit():
        a = int(num1)
        b = int(num2)
        p=1-b/100
        res = a/p

        return render(request, "result.html", {"result": res})
    else:
        res = "Не корректно введены данные"
        return render(request, "result.html", {"result": res})

def ind(request):
    return render(request, "rentab.html")