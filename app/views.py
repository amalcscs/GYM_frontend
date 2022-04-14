
from django.shortcuts import render, redirect

from django.conf import settings

def  Main_page(request):
    return render(request, 'Main_page.html')


############# Anandhu Dashboard Section ##############

def SuperAdminGYM_index(request):
    return render(request,'SuperAdminGYM_index.html')

def SuperAdminGYM_Dashboard(request):
    return render(request,'SuperAdminGYM_Dashboard.html')    

def SuperAdminGYM_Total_Instructors(request):
    return render(request,'SuperAdminGYM_Total_Instructors.html')    

def SuperAdminGYM_TotalTraineesUPhysicalTrainer(request):
    return render(request,'SuperAdminGYM_TotalTraineesUPhysicalTrainer.html')    

def SuperAdminGYM_TotalTraineesUPhysicalTrainer2(request):
    return render(request,'SuperAdminGYM_TotalTraineesUPhysicalTrainer2.html')

def SuperAdminGYM_TraineeProfile(request):
    return render(request,'SuperAdminGYM_TraineeProfile.html')  

def SuperAdminGYM_TraineeProfile1(request):
    return render(request,'SuperAdminGYM_TraineeProfile1.html')  

############# Anandhu Dashboard Section ends ############## 

############# Anandhu Batch Section  ############## 

def SuperAdminGYM_Batch(request):
    return render(request,'SuperAdminGYM_Batch.html')     

############# Anandhu Batch Section ends ############## 

############# Praveen Dashboard Section ##############

def SuperAdmin_trainees(request):
    return render(request,'SuperAdmin_trainees.html')

def SuperAdmin_ActiveTrainees(request):
    return render(request,'SuperAdmin_ActiveTrainees.html')

def SuperAdmin_PassiveTrainees(request):
    return render(request,'SuperAdmin_PassiveTrainees.html')

def SuperAdmin_ActiveTraineeProfile(request):
    return render(request,'SuperAdmin_ActiveTrainerProfile.html')

def SuperAdmin_PassiveTraineeProfile(request):
    return render(request,'SuperAdmin_PassiveTrainerProfile.html')

def SuperAdmin_Machines(request):
    return render(request,'SuperAdmin_Machines.html')

############# Praveen Dashboard Section ends ##############
   
############# Nimisha Expense Section ##############


def SuperAdmin_Expense(request):
    return render(request,'SuperAdmin_Expense.html')

def SuperAdmin_ExpenseView(request):
    return render(request,'SuperAdmin_ExpenseView.html')

def SuperAdmin_NewTransaction(request):
    return render(request,'SuperAdmin_NewTransaction.html')

def SuperAdmin_ExpenseViewEdit(request):
    return render(request,'SuperAdmin_ExpenseViewEdit.html')

def SuperAdmin_FindExpense(request):
    return render(request,'SuperAdmin_FindExpense.html')

def SuperAdmin_FindExpenseView(request):
    return render(request,'SuperAdmin_FindExpenseView.html')

def SuperAdmin_FindExpenseViewEdit(request):
    return render(request,'SuperAdmin_FindExpenseViewEdit.html')

def SuperAdmin_FindExpenseNewTransaction(request):
    return render(request,'SuperAdmin_FindExpenseNewTransaction.html')

############# Nimisha Expense Section ends ############## 


############ Sanjay Machine Section #####################


def gymmachine(request):
    return render(request,'gymmachine.html')    


def addcategory(request):
    return render(request,'addcategory.html') 


def viewcategory(request):
    return render(request,'viewcategory.html')    


def viewmachines(request):
    return render(request,'viewmachines.html')     

def chestpressmachine(request):
    return render(request,'chestpressmachine.html')

def dumbbell(request):
    return render(request,'dumbbell.html')


def preacher(request):
    return render(request,'preacher.html')    


def legpress(request):
    return render(request,'legpress.html')     


def form(request):
    return render(request,'form.html')


def chestview(request):
    return render(request,'chestview.html')


def shoulderview(request):
    return render(request,'shoulderview.html')

def triceps(request):
    return render(request,'triceps.html')

def bicepsview(request):
    return render(request,'bicepsview.html')


########### Sanjay Machine Section End ###########

############ Unnikrishnan Workout Section #####################


def superadmin_workout(request):
    return render(request,'superadmin_workout.html')

def superadmin_viewworkout(request):
    return render(request,'superadmin_viewworkout.html')

def superadmin_addworkout(request):
    return render(request,'superadmin_addworkout.html')

def superadmin_ChestDetailView(request):
    return render(request,'superadmin_ChestDetailView.html')

def superadmin_BackDetailView(request):
    return render(request,'superadmin_BackDetailView.html')

############## Unnikrishnan workout section end ################


############# Subeesh Payment Section ##############



def SuperAdmin_pay_det(request):
     return render(request, 'SuperAdmin_pay_det.html')

def SuperAdmin_current_trainees(request):
     return render(request, 'SuperAdmin_current_trainees.html')

def SuperAdmin_current_trainees_payment(request):
     return render(request, 'SuperAdmin_current_trainees_payment.html')

def SuperAdmin_current_trainees_payment_add(request):
     return render(request, 'SuperAdmin_current_trainees_payment_add.html')

def SuperAdmin_current_trainees_payment_update(request):
     return render(request, 'SuperAdmin_current_trainees_payment_update.html')

def SuperAdmin_previous_trainees_payment(request):
     return render(request, 'SuperAdmin_previous_trainees_payment.html')




############# Subeesh Payment Section ends ##############




############# Akhil Physical Trainer Section ##############

def SuperAdmin_personal_trainer(request):
    return render(request,'SuperAdmin_personal_trainer.html')

def SuperAdmin_active_trainers(request):
    return render(request,'SuperAdmin_active_trainers.html')

def SuperAdmin_resigned_trainers(request):
    return render(request,'SuperAdmin_resigned_trainers.html')

def SuperAdmin_activetrainer_update(request):
    return render(request,'SuperAdmin_activetrainer_update.html')

def SuperAdmin_resignedtrainer_update(request):
    return render(request,'SuperAdmin_resignedtrainer_update.html')


############# Akhil Physical Trainer Section ends ##############


############# Anwar Rgistration Section ##############


def SuperAdmin_RegistrationDetails(request):
    return render(request,'SuperAdmin_RegistrationDetails.html')
def SuperAdmin_Activereg(request):
    return render(request,'SuperAdmin_Activereg.html')
def SuperAdmin_Updatereg(request):
    return render(request,'SuperAdmin_Updatereg.html') 
def SuperAdmin_Passivereg(request):
    return render(request,'SuperAdmin_Passivereg.html') 
def SuperAdmin_PassiveUpdate(request):
    return render(request,'SuperAdmin_PassiveUpdate.html') 


############# Anwar Rgistration Section ends ##############


#***************************  Trainer module *************************

def Trainer_index(request):
    return render(request, 'Trainer_index.html')
  
def Trainer_Trainees_card(request):
    return render(request,'Trainer_Trainees_card.html')

def Trainer_Current_Trainees_table(request):
    return render(request,'Trainer_Current_Trainees_table.html')

def Trainer_Current_Trainees_profile(request):
    return render(request,'Trainer_Current_Trainee_profile.html')

def Trainer_Current_Trainees_profile1(request):
    return render(request,'Trainer_Current_Trainee_profile1.html')

def Trainer_Previous_Trainees_table(request):
    return render(request,'Trainer_Previous_Trainees_table.html')

def Trainer_Previous_Trainees_profile(request):
    return render(request,'Trainer_Previous_Trainee_profile.html')

def Trainer_Previous_Trainees_profile1(request):
    return render(request,'Trainer_Previous_Trainees_profile1.html')

#***************************  Nidhun *************************

def Trainer_dashboard(request):
    return render(request,'Trainer_dashboard.html')

#***************************  Anwar *************************

def Trainer_Paymenthistory(request):
    return render(request,'Trainer_Paymenthistory.html')


#***************************  Trainee module *************************

#***************************  Unnikrishnan *************************

def Trainee_index(request):
    return render(request,'Trainee_index.html')

def Trainee_Dashboard(request):
    return render(request,'Trainee_Dashboard.html')

#***************************  Akhil *************************

def Trainee_payment_history(request):
    return render(request,'Trainee_payment_history.html')



#*********************meenu**************
def workout(request):
    return render(request,'workout.html')

def workoutdetails(request):
    return render(request,'workoutdetails.html')

def workoutdetails2(request):
    return render(request,'workoutdetails2.html')

def trainerworkout(request):
    return render(request,'trainerworkout.html')

def trainerworkoutdetails(request):
    return render(request,'trainerworkdetails.html')

def trainerworkoutdetails2(request):
    return render(request,'trainerworkoutdetails2.html')