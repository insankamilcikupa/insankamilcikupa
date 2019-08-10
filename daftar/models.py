from django.db import models

# Create your models here.

choices2 = (
    ('sd','SD'),
    ('smp','SMP'),
    ('sma','SMA'),
    ('s1','S1'),
    ('s2','S2'),
    ('s3','S3'),
)

class DaftarModel(models.Model):
    nama_lengkap    = models.CharField(max_length=50, blank=False, null=False)
    tanggal_lahir   = models.DateField(blank=False, null=False)
    tempat_lahir    = models.CharField(max_length=20, blank=False, null=False)
    choices1 = (
        ('pria','Pria'),
        ('wanita','Wanita'),
        )
    jenis_kelamin   = models.CharField(
        max_length=10, 
        choices = choices1,
        default = 'pria',
        )

    alamat          = models.CharField(max_length=50, blank=False, null=False)
    nama_ayah       = models.CharField(max_length=50, blank=False, null=False)
    pekerjaan_ortu  = models.CharField(max_length=20, blank=False, null=False)
    pendidikan_ortu = models.CharField(max_length=15, choices = choices2)

    published       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}. {}".format(self.id, self.nama_lengkap)