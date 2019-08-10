from django.conf.urls import url

from .import views

urlpatterns = [
    url(r'^daftar_siswa/$', views.daftar_siswa),
]