from django.shortcuts import render

# Create your views here.
def condition(request):
    d = {'a':100,'b':20,'c':300}
    return render(request,'conditions.html',d)