from django.shortcuts import render

# Create your views here.
def app1fun(request):
    return render(request,'app1/one.html')