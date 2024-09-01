from django.shortcuts import render

def home(request):
    return render(request,"Sasikiran_Dommara.html")

def about(request):
    return render(request,"about.html")
def skills(request):
    return render(request,"skills.html")
def projects(request):
    return render(request,"projects.html")
