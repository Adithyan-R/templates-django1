
from django.urls import path
from app2 import views
app_name='app2'
urlpatterns = [
    path('app2fun/',views.app2fun,name='app2fun'),
]