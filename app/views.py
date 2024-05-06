from django.shortcuts import render

# Create your views here.

def main_view(request):
    return render(request,'main.html')

def edu_view(request):
    return render(request,'edu.html')

def skill_view(request):
    return render(request,'skill.html')

def project_view(request):
    return render(request,'project.html')

def details_view(request):
    return render(request,'details.html')

def contact_view(request):
    return render(request,'contact.html')