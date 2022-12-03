from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # Deliverables:
    path('units/unit1', views.unit1, name='unit1'),
    path('units/unit2', views.unit2, name='unit2'),
    path('units/unit3', views.unit3, name='unit3'),
    path('units/unit4', views.unit4, name='unit4'),


    # Auth:
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', views.login, name='login'),
]