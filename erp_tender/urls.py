"""
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

import tender.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', tender.views.Index, name='home'),




    path('users/', include('tender.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = '«Административная часть менеджера задач. Хвала и почет ВЕЛИКОМУ ARK!»'

admin.site.site_title = 'Админка'

admin.site.index_title = 'ARK рад Вам!'