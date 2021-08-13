from django.shortcuts import render

# Create your views here.
def app2fun(request):
    return render(request,'app2/two.html')