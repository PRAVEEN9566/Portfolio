from django.urls import path
from app import views

urlpatterns = [
    path('main/',views.main_view,name='main'),
    path('edu/',views.edu_view,name='edu'),
    path('skill/',views.skill_view,name='skill'),
    path('project/',views.project_view,name='pro'),
    path('details/',views.details_view,name='details'),
    path('contact',views.contact_view,name='contact'),
]
