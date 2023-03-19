from django.shortcuts import redirect, render

# Create your views here.
def homepage(request):
    return render(request, 'landing_page.html')

def login(request):
    return render(request, 'login_page.html')