from django.urls import path
from . import views


urlpatterns = [
    path('', views.CalculatorView.as_view(), name='calc'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    # Called by form to create dependent select droplist
    path('ajax/load-types/', views.load_types, name='ajax_load_types'), 
] 