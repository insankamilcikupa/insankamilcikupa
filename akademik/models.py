from django.db import models
from django.utils.text import slugify
# Create your models here.


class Siswa(models.Model):
    nis = models.CharField(max_length=8)
    nama = models.CharField(max_length=50)
    tempat_lahir = models.CharField(max_length=15)
    kelas = models.CharField(max_length=2, blank=True)
    waktuEdit = models.DateTimeField(auto_now_add = True)
    slug = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.nama)
        super(Siswa, self).save()

    def __str__(self):
        return "{}. {}".format(self.id, self.nama)

class Guru(models.Model):
    nik = models.CharField(max_length=10)
    nama = models.CharField(max_length=50)
    tempat_lahir = models.CharField(max_length=15)
    alamat = models.CharField(max_length=50)

    def __str__(self):
        return "{}. {}".format(self.id, self.nama)

