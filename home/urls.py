from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('faq/', views.faq, name='faq'),
    path('our_philosophy/', views.our_philosophy, name='our_philosophy'),
]
