from django.urls import path
from salesforce import views

urlpatterns = [
    path('push', views.PutData, name='PutData'),
    path('pull', views.PullData, name='PullData'),
]
