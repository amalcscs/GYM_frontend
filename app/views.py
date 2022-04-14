
from django.shortcuts import render, redirect

from django.conf import settings

 
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
