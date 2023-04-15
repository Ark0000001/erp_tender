from .models import Tab, DealerTab, IconsDealers, PostavTab, Product, ControlProduct, Info, TenderTab, Gruz

from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import UserCreationForm
import logging
from django.core.management import call_command
import datetime
import openai
from django.conf import settings


def chatbot(request):
    chatbot_response = None

    if request.method == 'POST':
        openai.api_key = settings.KEY_OPENAI
        user_input = request.POST.get('chatbot')
        prompt=user_input

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,  # use the updated prompt variable here
            max_tokens=1024,


            temperature=0.5,
        )


        chatbot_response=response['choices'][0]['text']

    return render(request, 'chat_bot.html', {'response': chatbot_response})

logger = logging.getLogger('main')


def trial(request):
    call_command('dbbackup')
    return print('db created! - ')


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


def Index(request):
    tabs = Tab.objects.filter(is_active=False).order_by('data2')
    context = {'tabs': tabs, 'now': datetime.datetime.now()}
    return render(request, 'home.html', context)


def Index_Cit(request):
    tabs = Tab.objects.filter(is_active=False, staffer__name__istartswith='Ситник').order_by('data2')
    context = {'tabs': tabs, 'now': datetime.datetime.now()}
    return render(request, 'cit.html', context)


def Index_Kal(request):
    icond = IconsDealers.objects.all()
    tabs = Tab.objects.filter(is_active=False, staffer__name__istartswith='Кальницкий').order_by('data2')
    context = {'tabs': tabs, 'icond': icond, 'now': datetime.datetime.now()}
    return render(request, 'kal.html', context)


def Index_Mur(request):
    tabs = Tab.objects.filter(is_active=False, staffer__name__istartswith='Муромцева').order_by('data2')
    context = {'tabs': tabs, 'now': datetime.datetime.now()}
    return render(request, 'mur.html', context)


def Index_Pel(request):
    tabs = Tab.objects.filter(is_active=False, staffer__name__istartswith='Пелых').order_by('data2')
    context = {'tabs': tabs, 'now': datetime.datetime.now()}
    return render(request, 'pel.html', context)


def Index_Skor(request):
    tabs = Tab.objects.filter(is_active=False, staffer__name__istartswith='Скоробогатая').order_by('data2')
    context = {'tabs': tabs, 'now': datetime.datetime.now()}
    return render(request, 'skor.html', context)

def Index_Glu(request):
    tabs = Tab.objects.filter(is_active=False, staffer__name__istartswith='Глухова').order_by('data2')
    context = {'tabs': tabs, 'now': datetime.datetime.now()}
    return render(request, 'glu.html', context)


def Index_Mir(request):
    tabs = Tab.objects.filter(is_active=False, staffer__name__istartswith='Мирончик').order_by('data2')
    context = {'tabs': tabs, 'now': datetime.datetime.now()}
    return render(request, 'mir.html', context)


def Index_Evt(request):
    # tabs = Tab.objects.filter(is_active=False, staffer__name__istartswith='Евтеев').order_by('data2')
    # context = {'tabs': tabs,'now': datetime.datetime.now()}
    tabs = Tab.objects.filter(is_active=False, staffer__name__istartswith='Евтеев').order_by('data2')

    context = {'tabs': tabs, 'now': datetime.datetime.now()}
    return render(request, 'evt.html', context)


def addition(request):
    def is_number(str):
        try:
            float(str)
            return True
        except ValueError:
            return False

    num1 = request.POST['num1'].replace(',', '.')
    num2 = request.POST['num2'].replace(',', '.')
    num3 = request.POST['num3'].replace(',', '.')
    num666 = request.POST['num666'].replace(',', '.')

    if is_number(num1) and is_number(num2) and is_number(num3) and is_number(num666):
        v = float(num1)
        s = float(num2) + float(num666)
        r = float(num3)

        if r > 0 and v > 0:
            pri1 = r * v / 100
            pri = f"Прибыль = {pri1:.2f}"
        elif s > 0 and v > 0:
            pri1 = v - s
            pri = f"Прибыль = {pri1:.2f}"
        else:
            pri = f"Прибыль = нет данных"

        if v > 0 and s > 0:
            p = v - s
            rent1 = p / v * 100
            rent = f"Рентабельность = {rent1:.2f}"
        else:
            rent = f"Рентабельность = {r}"

        if r > 0 and v > 0:
            p = r * v / 100
            ss1 = v - p
            ss = f"Себестоимость = {ss1:.2f}"
        else:
            ss = f"Себестоимость = {s}"

        if s > 0 and r > 0:
            vyr1 = s / (1 - r / 100)
            pri1=vyr1-s
            pri = f"Прибыль = {pri1:.2f}"
            vyr = f"Выручка = {vyr1:.2f}"
        else:
            vyr = f"Выручка = {v:.2f}"

        if v > 0 and s > 0:
            nac1 = v * 100 / s - 100
            nac = f"Наценка = {nac1:.2f}"
        elif v > 0 and r > 0:
            p = r * v / 100
            s = v - p
            nac1 = v * 100 / s - 100
            nac = f"Наценка = {nac1:.2f}"
        elif s > 0 and r > 0:
            v = s / (1 - r / 100)
            nac1 = v * 100 / s - 100
            nac = f"Наценка = {nac1:.2f}"
        else:
            nac = f"Наценка = нет данных"



        context = {"num1": num1, "num2": num2, "num3": num3, "pri": pri, "rent": rent, "ss": ss, "vyr": vyr, "nac": nac,
                   "num666": num666}
        return render(request, "result.html", context)
    else:
        pri = "Не корректно введены данные"
        rent = "Не корректно введены данные"
        ss = "Не корректно введены данные"
        vyr = "Не корректно введены данные"
        nac = "Не корректно введены данные"
        context = {"num1": num1, "num2": num2, "num3": num3, "pri": pri, "rent": rent, "ss": ss, "vyr": vyr, "nac": nac,
                   "num666": num666}
        return render(request, "result.html", context)


# def pri(request):
#
#     num1 = request.POST['num1']
#     num2 = request.POST['num2']
#     num11 = num1.replace('.', '')
#     num22 = num2.replace('.', '')
#     if num11.isdigit() and num22.isdigit():
#         a = float(num1)
#         b = float(num2)
#         p=a*b/100
#         res = p
#
#         return render(request, "result.html", {"result": res})
#     else:
#         res = "Не корректно введены данные"
#         return render(request, "result.html", {"result": res})

# def seb(request):
#
#     num1 = request.POST['num1']
#     num2 = request.POST['num2']
#     num11 = num1.replace('.', '')
#     num22 = num2.replace('.', '')
#     if num11.isdigit() and num22.isdigit():
#         a = float(num1)
#         b = float(num2)
#         p=a*b/100
#         res = b-p
#
#         return render(request, "result.html", {"result": res})
#     else:
#         res = "Не корректно введены данные"
#         return render(request, "result.html", {"result": res})

# def vyr(request):
#
#     num1 = request.POST['num1']
#     num2 = request.POST['num2']
#     num11=num1.replace('.','')
#     num22 = num2.replace('.', '')
#     if num11.isdigit() and num22.isdigit():
#         a = float(num1)
#         b = float(num2)
#         p=1-b/100
#         res = a/p
#
#         return render(request, "result.html", {"result": res})
#     else:
#         res = "Не корректно введены данные"
#         return render(request, "result.html", {"result": res})

# def nac(request):
#
#     num1 = request.POST['num1']
#     num2 = request.POST['num2']
#     num11 = num1.replace('.', '')
#     num22 = num2.replace('.', '')
#     if num11.isdigit() and num22.isdigit():
#         a = float(num1)
#         b = float(num2)
#         p=a*100/b
#         res = p-100
#
#         return render(request, "result.html", {"result": res})
#     else:
#         res = "Не корректно введены данные"
#         return render(request, "result.html", {"result": res})

def ind(request):
    return render(request, "rentab.html")


def dealerTab(request):
    # logger.info('Зашли в дилеры')
    # icond=IconsDealers.objects.all()
    tasks = DealerTab.objects.filter(is_active_tasks=True).order_by('task_info')

    tabs = DealerTab.objects.filter(is_active=False).order_by('company')
    context = {'tabs': tabs, 'tasks': tasks, 'now': datetime.datetime.now()}
    return render(request, 'dealer.html', context)


def postavTab(request):
    # icond=IconsDealers.objects.all()
    # a=datetime.date.today()
    # bb = datetime.timedelta(days=int(PostavTab)))
    # cc=a+bb
    # srok=cc-a

    tasks = PostavTab.objects.filter(is_active_tasks=True).order_by('task_info')
    tabs = PostavTab.objects.filter(is_active=False).order_by('dogovor','organizations')
    context = {'tabs': tabs, 'tasks': tasks, 'now': datetime.datetime.now()}
    return render(request, 'postavschiki.html', context)


def prodTab(request):
    tabs = Product.objects.order_by('-raznica2')
    context = {'tabs': tabs, 'now': datetime.datetime.now()}
    return render(request, 'pereschet.html', context)


def controlProd(request):
    tabs = ControlProduct.objects.order_by('product')
    context = {'tabs': tabs, 'now': datetime.datetime.now()}
    return render(request, 'controlprod.html', context)


def poisk(request):
    num1 = request.POST['tovar']
    tabs = Product.objects.filter(Q(name__icontains=num1)).order_by('name')

    context = {"tabs": tabs}
    return render(request, "poisk.html", context)


def info(request):
    tabs = Info.objects.order_by('-updated')

    context = {"tabs": tabs}
    return render(request, "info.html", context)


def poisk_tasks(request):
    num1 = request.POST['task_info']
    tabs = Tab.objects.filter(is_active=False).filter(
        Q(task_info__icontains=num1) | Q(id__icontains=num1) | Q(profit_info__icontains=num1)).order_by('data2')

    context = {"tabs": tabs}
    return render(request, "poisk_tasks.html", context)
def poisk_tasks_arhiv_z(request):
    num1 = request.POST['task_info_arhiv_z']
    tabs = Tab.objects.filter(is_active=True).filter(
        Q(task_info__icontains=num1) | Q(id__icontains=num1) | Q(profit_info__icontains=num1)).order_by('-data2')

    context = {"tabs": tabs}
    return render(request, "poisk_tasks_arhiv_z.html", context)


def tenderTab(request):
    tabs = TenderTab.objects.filter(is_active=False).order_by('data_win')
    tasks = Tab.objects.filter(is_active=False).order_by('data2')
    context = {'tabs': tabs, 'tasks': tasks, 'now': datetime.datetime.now()}
    return render(request, 'tender.html', context)


def penya(request):
    num1 = request.POST['num1']
    num2 = request.POST['num2']
    num3 = request.POST['num3']

    while True:
        try:
            summa_prosr = num1
            summa_prosr = float(summa_prosr.replace(",", "."))
            break
        except:
            return render(request, "error.html")

    while True:
        try:
            dni_prosr = num2
            dni_prosr = int(dni_prosr)
            break
        except:
            return render(request, "error.html")

    while True:
        try:
            stavka_refin = num3
            stavka_refin = float(stavka_refin.replace(",", "."))
            break
        except:
            return render(request, "error.html")


    peny = round(summa_prosr * dni_prosr * 1 / 300 * stavka_refin / 100, 2)
    if peny == 0:
        peny = 'Некрректно введены данные'
        context = {"num1": num1, "num2": num2, "num3": num3, "peny": peny}
        return render(request, "result_peny.html", context)

    else:
        peny=peny
        context = {"num1": num1, "num2": num2, "num3": num3, "peny": peny}
        return render(request, "result_peny.html", context)


def ind_peny(request):
    return render(request, "peny.html")


def gruzTab(request):
    tabs = Gruz.objects.filter(is_active=False).order_by('data_gruz')

    context = {'tabs': tabs}
    return render(request, 'gruz.html', context)

def arhiv_z(request):
    tabs = Tab.objects.filter(is_active=True).order_by('-data2')
    context = {'tabs': tabs}
    return render(request, 'arhiv_z.html', context)