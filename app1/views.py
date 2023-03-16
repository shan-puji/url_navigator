from django.shortcuts import render

# Create your views here.
def sample1(request):
    d={'name':'chintu','age':58}
    return render(request,'sample1.html',d)
