
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

    ########### Anandhu Dashboard Section ##########
           
    re_path(r'^SuperAdminGYM_index$', views.SuperAdminGYM_index, name='SuperAdminGYM_index'),
    re_path(r'^SuperAdminGYM_Dashboard$', views.SuperAdminGYM_Dashboard, name='SuperAdminGYM_Dashboard'),
    re_path(r'^SuperAdminGYM_Total_Instructors$', views.SuperAdminGYM_Total_Instructors, name='SuperAdminGYM_Total_Instructors'),
    re_path(r'^SuperAdminGYM_TotalTraineesUPhysicalTrainer$', views.SuperAdminGYM_TotalTraineesUPhysicalTrainer, name='SuperAdminGYM_TotalTraineesUPhysicalTrainer'),
    re_path(r'^SuperAdminGYM_TotalTraineesUPhysicalTrainer2$', views.SuperAdminGYM_TotalTraineesUPhysicalTrainer2, name='SuperAdminGYM_TotalTraineesUPhysicalTrainer2'),
    re_path(r'^SuperAdminGYM_TraineeProfile$', views.SuperAdminGYM_TraineeProfile, name='SuperAdminGYM_TraineeProfile'),
    re_path(r'^SuperAdminGYM_TraineeProfile1$', views.SuperAdminGYM_TraineeProfile1, name='SuperAdminGYM_TraineeProfile1'),
    
        ########### Anandhu Dashboard Section ##########

        ########### Anandhu Batch Section ##########  

    re_path(r'^SuperAdminGYM_Batch$', views.SuperAdminGYM_Batch, name='SuperAdminGYM_Batch'),

        ########### Anandhu Batch Section ends ##########

        ############# Praveen Dashboard Section ##############
    
    re_path(r'^SuperAdmin_trainees/$', views.SuperAdmin_trainees, name='SuperAdmin_trainees'),
    re_path(r'^SuperAdmin_ActiveTrainees/$', views.SuperAdmin_ActiveTrainees, name='SuperAdmin_ActiveTrainees'),
    re_path(r'^SuperAdmin_PassiveTrainees/$', views.SuperAdmin_PassiveTrainees, name='SuperAdmin_PassiveTrainees'),
    re_path(r'^SuperAdmin_ActiveTraineeProfile/$', views.SuperAdmin_ActiveTraineeProfile, name='SuperAdmin_ActiveTraineeProfile'),
    re_path(r'^SuperAdmin_PassiveTraineeProfile/$', views.SuperAdmin_PassiveTraineeProfile, name='SuperAdmin_PassiveTraineeProfile'),
    re_path(r'^SuperAdmin_Machines/$', views.SuperAdmin_Machines, name='SuperAdmin_Machines'),
    
        ############# Praveen Dashboard Section ends ##############

        ############# Nimisha Expense Section ##############

    re_path(r'^SuperAdmin_Expense$',views.SuperAdmin_Expense,name='SuperAdmin_Expense'),
    re_path(r'^SuperAdmin_ExpenseView$',views.SuperAdmin_ExpenseView,name='SuperAdmin_ExpenseView'),
    re_path(r'^SuperAdmin_NewTransaction$',views.SuperAdmin_NewTransaction,name='SuperAdmin_NewTransaction'),
    re_path(r'^SuperAdmin_ExpenseViewEdit$',views.SuperAdmin_ExpenseViewEdit,name='SuperAdmin_ExpenseViewEdit'),
    re_path(r'^SuperAdmin_FindExpense$',views.SuperAdmin_FindExpense,name='SuperAdmin_FindExpense'),
    re_path(r'^SuperAdmin_FindExpenseView$',views.SuperAdmin_FindExpenseView,name='SuperAdmin_FindExpenseView'),
    re_path(r'^SuperAdmin_FindExpenseViewEdit$',views.SuperAdmin_FindExpenseViewEdit,name='SuperAdmin_FindExpenseViewEdit'),
    re_path(r'^SuperAdmin_FindExpenseNewTransaction$',views.SuperAdmin_FindExpenseNewTransaction,name='SuperAdmin_FindExpenseNewTransaction'),

        ############# Nimisha Expense Section ends ############## 

        ############# Sanjay Machine Section   ##################
    re_path(r'^gymmachine$', views.gymmachine, name='gymmachine'),
    re_path(r'^addcategory$', views.addcategory, name='addcategory'),
    re_path(r'^viewcategory$', views.viewcategory, name='viewcategory'),
    re_path(r'^viewmachines$', views.viewmachines, name='viewmachines'),
    re_path(r'^chestpressmachine$', views.chestpressmachine, name='chestpressmachine'),
    re_path(r'^dumbbell$', views.dumbbell, name='dumbbell'),
    re_path(r'^preacher$', views.preacher, name='preacher'),
    re_path(r'^legpress$', views.legpress, name='legpress'),
    re_path(r'^form$', views.form, name='form'),
    re_path(r'^chestview$', views.chestview, name='chestview'),
    re_path(r'^shoulderview$', views.shoulderview, name='shoulderview'),
    re_path(r'^triceps$', views.triceps, name='triceps'),
    re_path(r'^bicepsview$', views.bicepsview, name='bicepsview'),

    ###############  Sanjay Machine Section Ends #################

    ############### Unnikrishnan workout section #################
    re_path(r'^superadmin_workout$',views.superadmin_workout,name='superadmin_workout'),
    re_path(r'^superadmin_viewworkout$',views.superadmin_viewworkout,name='superadmin_viewworkout'),
    re_path(r'^superadmin_addworkout$',views.superadmin_addworkout,name='superadmin_addworkout'),
    re_path(r'^superadmin_ChestDetailView$',views.superadmin_ChestDetailView,name='superadmin_ChestDetailView'),
    re_path(r'^superadmin_BackDetailView$',views.superadmin_BackDetailView,name='superadmin_BackDetailView'),

    ############### Unnikrishnan workout section ends #################

############# subeesh payment Section ##############

    re_path(r'^SuperAdmin_pay_det/$', views.SuperAdmin_pay_det, name='SuperAdmin_pay_det'),
    re_path(r'^SuperAdmin_current_trainees/$', views.SuperAdmin_current_trainees, name='SuperAdmin_current_trainees'),
    re_path(r'^SuperAdmin_current_trainees_payment/$', views.SuperAdmin_current_trainees_payment, name='SuperAdmin_current_trainees_payment'),
    re_path(r'^SuperAdmin_current_trainees_payment_add/$', views.SuperAdmin_current_trainees_payment_add, name='SuperAdmin_current_trainees_payment_add'),
    re_path(r'^SuperAdmin_current_trainees_payment_update/$', views.SuperAdmin_current_trainees_payment_update, name='SuperAdmin_current_trainees_payment_update'),
    re_path(r'^SuperAdmin_previous_trainees_payment/$', views.SuperAdmin_previous_trainees_payment, name='SuperAdmin_previous_trainees_payment'),


    ############# subeesh payment Section ends ##############

    ############# Akhil Physical Trainer Section ##############

    re_path(r'^SuperAdmin_personal_trainer/$', views.SuperAdmin_personal_trainer, name='SuperAdmin_personal_trainer'),
    re_path(r'^SuperAdmin_active_trainers/$', views.SuperAdmin_active_trainers, name='SuperAdmin_active_trainers'),
    re_path(r'^SuperAdmin_resigned_trainers/$', views.SuperAdmin_resigned_trainers, name='SuperAdmin_resigned_trainers'),
    re_path(r'^SuperAdmin_activetrainer_update/$', views.SuperAdmin_activetrainer_update, name='SuperAdmin_activetrainer_update'),
    re_path(r'^SuperAdmin_resignedtrainer_update/$', views.SuperAdmin_resignedtrainer_update, name='SuperAdmin_resignedtrainer_update'),




    ############# Akhil Physical Trainer Section ends ##############


    ############# Anwar Rgistration Section ##############

    re_path(r'^SuperAdmin_RegistrationDetails/$', views.SuperAdmin_RegistrationDetails, name='SuperAdmin_RegistrationDetails'),
    re_path(r'^SuperAdmin_Activereg/$', views.SuperAdmin_Activereg, name='SuperAdmin_Activereg'),
    re_path(r'^SuperAdmin_Updatereg/$', views.SuperAdmin_Updatereg, name='SuperAdmin_Updatereg'),
    re_path(r'^SuperAdmin_Passivereg/$', views.SuperAdmin_Passivereg, name='SuperAdmin_Passivereg'),
    re_path(r'^SuperAdmin_PassiveUpdate/$', views.SuperAdmin_PassiveUpdate, name='SuperAdmin_PassiveUpdate'),


    ############# Anwar Rgistration Section ends ##############



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

    
    
    #*********************meenu*********************
    re_path(r'^workout$',views.workout,name='workout'),
    re_path(r'^workoutdetails$',views.workoutdetails,name='workoutdetails'),
    re_path(r'^workoutdetails2$',views.workoutdetails2,name='workoutdetails2'),
    re_path(r'^trainerworkout$',views.trainerworkout,name='trainerworkout'),
    re_path(r'^trainerworkoutdetails$',views.trainerworkoutdetails,name='trainerworkoutdetails'),
    re_path(r'^trainerworkoutdetails2$',views.trainerworkoutdetails2,name='trainerworkoutdetails2')
    


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
