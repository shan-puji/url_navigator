from django.shortcuts import render

# Create your views here.
def sample2(request):
    d={'name':'jyothi','age':58}
    return render(request,'sample2.html',d)
