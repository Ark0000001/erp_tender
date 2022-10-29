from django.urls import path, include

from .views import *


# app_name = 'tender'
urlpatterns = [

    path('', include('django.contrib.auth.urls')),

    path('users/register/', Register.as_view(), name='register'),
    path('kal/', Index_Kal, name='kal'),
    path('cit/', Index_Cit, name='cit'),
    path('mur/', Index_Mur, name='mur'),
    path('skor/', Index_Skor, name='skor'),
    path('mir/', Index_Mir, name='mir'),
    path('evt/', Index_Evt, name='evt'),
    path('ind/',ind, name='ind'),
    path('ind/add', addition, name='add'),
    path('ind/pri', pri, name='pri'),
    path('ind/seb', seb, name='seb'),
    path('ind/vyr', vyr, name='vyr'),


]