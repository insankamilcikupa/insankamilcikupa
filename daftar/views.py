from django.shortcuts import render

# Create your views here.

from .forms import DaftarForm
from .models import DaftarModel

def daftar_siswa(request):
    daftar_form = DaftarForm(request.POST or None)
    if request.method == 'POST':
        if daftar_form.is_valid():
            daftar_form.save()


    context = {
        'heading':'Pendaftaran',
        'data_form':daftar_form,
    }
    return render(request, 'daftar/daftar.html', context)