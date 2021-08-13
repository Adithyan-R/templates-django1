from django.urls import path
from app1 import views
app_name='app1'
urlpatterns = [
    path('app1fun/',views.app1fun,name='app1fun'),
]