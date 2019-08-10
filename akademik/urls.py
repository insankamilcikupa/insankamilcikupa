from django.conf.urls import url

from .import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^siswa$', views.siswa),
    url(r'^kelas/(?P<kelasInput>[\w-]+)/$', views.kelasSiswa),
    url(r'^pendidik$', views.pendidik),
    url(r'^kalender$', views.kalender),
    url(r'^eskul$', views.eskul),
]