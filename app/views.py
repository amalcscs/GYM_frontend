
from django.shortcuts import render, redirect

from django.conf import settings
def  Main_page(request):
    return render(request, 'Main_page.html')
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
