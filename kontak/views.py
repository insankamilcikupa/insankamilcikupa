from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'kontak/kontak.html')

def kontak(request):
    return render(request,'kontak/kontak.html')