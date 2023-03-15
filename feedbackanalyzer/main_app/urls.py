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
    path('deliverables/', views.deliverables_index, name='index'),
    path('deliverables/<int:del_id>/', views.deliverable_detail, name='detail'),
    path('deliverables/newDeliverable/', views.DeliverableCreate.as_view(), name='deliverable_create'),
    path('deliverables/<int:pk>/update/', views.DeliverableUpdate.as_view(), name='deliverable_update'),
    path('deliverables/<int:pk>/delete/', views.DeliverableDelete.as_view(), name='deliverable_delete'),

    # Feedback Analysis:
    path('analyzer', views.analyzer, name='analyzer'),
    path('analyzer/unit1', views.unit1_feedback, name='analyzer_unit1'),
    path('analyzer/unit2', views.unit2_feedback, name='analyzer_unit2'),
    path('analyzer/unit3', views.unit3_feedback, name='analyzer_unit3'),
    path('analyzer/unit4', views.unit4_feedback, name='analyzer_unit4'),

    # Auth, Sign Up:  
    path('accounts/signup', views.signup, name='signup')
]