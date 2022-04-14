
from django.contrib import admin
from django.urls import re_path, include
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from app import views

urlpatterns = [

    re_path('admin/', admin.site.urls),
     re_path(r'^$', views.Main_page, name='Main_page'),
    ##############################  Trainer module ###############################

    re_path(r'^Trainer_index$', views.Trainer_index, name='Trainer_index'),
    re_path(r'^Trainer_Trainees_card/$', views.Trainer_Trainees_card, name='Trainer_Trainees_card'),
    re_path(r'^Trainer_Current_Trainees_table/$', views.Trainer_Current_Trainees_table, name='Trainer_Current_Trainees_table'),
    re_path(r'^Trainer_Current_Trainees_profile/$', views.Trainer_Current_Trainees_profile, name='Trainer_Current_Trainees_profile'),
    re_path(r'^Trainer_Current_Trainees_profile1/$', views.Trainer_Current_Trainees_profile1, name='Trainer_Current_Trainees_profile1'),
    re_path(r'^Trainer_Previous_Trainees_table/$', views.Trainer_Previous_Trainees_table, name='Trainer_Previous_Trainees_table'),
    re_path(r'^Trainer_Previous_Trainees_profile/$', views.Trainer_Previous_Trainees_profile, name='Trainer_Previous_Trainees_profile'),
    re_path(r'^Trainer_Previous_Trainees_profile1/$', views.Trainer_Previous_Trainees_profile1, name='Trainer_Previous_Trainees_profile1'),

    #-------------------------  Nidhun ----------------------------------

    re_path(r'^Trainer_dashboard$',views.Trainer_dashboard,name='Trainer_dashboard'),

    #-------------------------  Anwar ------------------------------------

    re_path(r'^Trainer_Paymenthistory/$', views.Trainer_Paymenthistory, name='Trainer_Paymenthistory'),

    #################################  Trainee module  ################################

    #---------------------------  Unnikrishnan ---------------------------------

    re_path(r'^Trainee_index$',views.Trainee_index,name='Trainee_index'),
    re_path(r'^Trainee_Dashboard$',views.Trainee_Dashboard,name='Trainee_Dashboard'),

    #---------------------------  Akhil ---------------------------------

    re_path(r'^Trainee_payment_history/$', views.Trainee_payment_history, name='Trainee_payment_history'),

    
    
    
    


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
