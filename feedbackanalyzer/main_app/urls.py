from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # Units:
    path('units/unit1', views.unit1, name='unit1'),
    path('units/unit2', views.unit2, name='unit2'),
    path('units/unit3', views.unit3, name='unit3'),
    path('units/unit4', views.unit4, name='unit4'),

    # Deliverables:
    path('deliverables/', views.deliverables_index, name='deliverable_view'),
    path('deliverables/newDeliverable/', views.DeliverableCreate.as_view(), name='deliverable_create'),

    # path('analyzer', views.analyzer, name='analyzer'),


    # Auth:
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', views.login, name='login'),
]