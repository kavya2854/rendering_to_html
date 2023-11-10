from django.shortcuts import render

# Create your views here.
def first_html(request):
    return render(request,'first.html')

def second_html(request):
    return render(request,'second.html')

def third_html(request):
    return render(request,'third.html')

def fourth_html(request):
    return render(request,'fourth.html')
