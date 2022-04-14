
from django.contrib import admin
from django.urls import re_path, include
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from app import views

urlpatterns = [

    re_path('admin/', admin.site.urls),
    re_path(r'^$', views.Trainer_index, name='Trainer_index'),
    re_path(r'^Trainer_Trainees_card/$', views.Trainer_Trainees_card, name='Trainer_Trainees_card'),
    re_path(r'^Trainer_Current_Trainees_table/$', views.Trainer_Current_Trainees_table, name='Trainer_Current_Trainees_table'),
    re_path(r'^Trainer_Current_Trainees_profile/$', views.Trainer_Current_Trainees_profile, name='Trainer_Current_Trainees_profile'),
    re_path(r'^Trainer_Current_Trainees_profile1/$', views.Trainer_Current_Trainees_profile1, name='Trainer_Current_Trainees_profile1'),
    re_path(r'^Trainer_Previous_Trainees_table/$', views.Trainer_Previous_Trainees_table, name='Trainer_Previous_Trainees_table'),
    re_path(r'^Trainer_Previous_Trainees_profile/$', views.Trainer_Previous_Trainees_profile, name='Trainer_Previous_Trainees_profile'),
    re_path(r'^Trainer_Previous_Trainees_profile1/$', views.Trainer_Previous_Trainees_profile1, name='Trainer_Previous_Trainees_profile1'),
    
    


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
