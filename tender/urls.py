from django.urls import path, include

from .views import *


# app_name = 'tender'
urlpatterns = [

    path('', include('django.contrib.auth.urls')),
    path('users/register/', Register.as_view(), name='register'),
    path('all_month/',IndexAll, name='all_month'),
    path('pdf/', generate_pdf_view,name='pdf'),
    path('kal/', Index_Kal, name='kal'),
    path('cit/', Index_Cit, name='cit'),
    path('mur/', Index_Mur, name='mur'),
    path('pel/', Index_Pel, name='pel'),
    path('glu/', Index_Glu, name='glu'),
    path('skor/', Index_Skor, name='skor'),
    path('mir/', Index_Mir, name='mir'),
    path('tur/', Index_Tur, name='tur'),
    path('evt/', Index_Evt, name='evt'),
    path('ind/',ind, name='ind'),
    path('ind/add', addition, name='add'),
    path('ind_peny/',ind_peny, name='ind_peny'),
    path('ind_peny/peny', penya, name='peny'),
    # path('ind/pri', pri, name='pri'),
    # path('ind/seb', seb, name='seb'),
    # path('ind/vyr', vyr, name='vyr'),
    # path('ind/nac', nac, name='nac'),
    path('dealer/', dealerTab, name='dealer'),
    path('postav/', postavTab, name='postav'),
    path('pereschet/', prodTab, name='pereschet'),
    path('contrprod/', controlProd, name='contrprod'),
    path('pereschet/poisk', poisk, name='poisk'),
    path('chatbot/chatbot', chatbot, name='chatbot'),
    path('info/',info, name='info'),
    path('info/<int:pk>/', InfoDetailView.as_view(), name='info_detail'),
    path('tags/<slug:tag_slug>/', TagIndexView.as_view(), name='posts_by_tag'),
    path('arhiv_z/',arhiv_z, name='arhiv_z'),
    path('zakaz/',zakazTab, name='zakaz'),
    path('poisk_tasks', poisk_tasks, name='poisk_tasks'),
    path('poisk_tasks_arhiv_z', poisk_tasks_arhiv_z, name='poisk_tasks_arhiv_z'),
    path('tender/', tenderTab, name='tender'),
    path('ucenka/', ucenka, name='ucenka'),
    path('gruz/', gruzTab, name='gruz'),


]