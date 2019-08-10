from django.shortcuts import render

# Create your views here.

from .models import Siswa
from .models import Guru

def index(request):
    return render(request,'akademik/index.html')

def siswa(request):
    siswa = Siswa.objects.all();
    context = {
        'Data': siswa,
    }
    return render(request, 'akademik/siswa.html', context)

def kelasSiswa(request, kelasInput):
    siswa = Siswa.objects.filter(kelas=kelasInput);
    kelas_data = Siswa.objects.values('kelas').distinct();
   
    context = {
        'kelas_data': kelas_data,
        'Data': siswa,
    }
    return render(request, 'akademik/kelas.html', context)


def pendidik(request):
    pendidik = Guru.objects.all();
    context = {
        'Data_Guru': pendidik,
    }
    return render(request, 'akademik/pendidik.html', context)

def kalender(request):
    return render(request, 'akademik/kalender.html')

def eskul(request):
    return render(request, 'akademik/eskul.html')

