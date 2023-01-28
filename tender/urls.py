from django.urls import path, include

from .views import *
import re


# app_name = 'tender'
urlpatterns = [

    path('', include('django.contrib.auth.urls')),
    path('users/register/', Register.as_view(), name='register'),
    path('kal/', Index_Kal, name='kal'),
    path('cit/', Index_Cit, name='cit'),
    path('mur/', Index_Mur, name='mur'),
    path('pel/', Index_Pel, name='pel'),
    path('skor/', Index_Skor, name='skor'),
    path('mir/', Index_Mir, name='mir'),
    path('evt/', Index_Evt, name='evt'),
    path('ind/',ind, name='ind'),
    path('ind/add', addition, name='add'),
    # path('ind/pri', pri, name='pri'),
    # path('ind/seb', seb, name='seb'),
    # path('ind/vyr', vyr, name='vyr'),
    # path('ind/nac', nac, name='nac'),
    path('dealer/', dealerTab, name='dealer'),
    path('postav/', postavTab, name='postav'),
    path('pereschet/', prodTab, name='pereschet'),
    path('contrprod/', controlProd, name='contrprod'),
    path('pereschet/poisk', poisk, name='poisk'),
    path('info/',info, name='info'),
    path('poisk_tasks', poisk_tasks, name='poisk_tasks'),
    path('tender/', tenderTab, name='tender'),


]