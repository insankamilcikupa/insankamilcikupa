from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'profil/index.html')

def profil(request):
    return render(request, 'profil/profil.html')