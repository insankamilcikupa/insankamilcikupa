from django import forms
from.models import DaftarModel

class DaftarForm(forms.ModelForm):
    class Meta:
        model = DaftarModel
        fields = [
            'nama_lengkap',
            'tanggal_lahir',
            'tempat_lahir',
            'jenis_kelamin',
            'alamat',
            'nama_ayah',
            'pekerjaan_ortu',
            'pendidikan_ortu',
        ]
        tahun = range(2000,2017,1)

        labels = {
            'nama_lengkap': 'Nama Lengkap',
            'tanggal_lahir': 'Tanggal Lahir',
            'tempat_lahir': 'Tempat Lahir',
            'jenis_kelamin': 'Jenis Kelamin',
            'alamat': 'Alamat Lengkap',
            'nama_ayah': 'Nama Ayah',
            'pekerjaan_ortu': 'Pekerjaan Ayah',
            'pendidikan_ortu': 'Pendidikan Ayah',
        }
        widgets = {
            'nama_lengkap': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Isi Nama Lengkap',
                }
            ),

           
            'tanggal_lahir': forms.SelectDateWidget(
                years = tahun,
                attrs = {
                    'class':'form-control col-row-sm-1',
                }
            ),

            'tempat_lahir': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Isi Tempat Lahir',
                }
            ),

            'jenis_kelamin': forms.Select(
                attrs = {
                    'class':'form-control col-sm-2',
                }
            ),

            'alamat': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Isi Alamat',
                }
            ),

            'nama_ayah': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Isi Nama Ayah',
                }
            ),

            'pekerjaan_ortu': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Isi Pekerjaan Ayah',
                }
            ),

            'pendidikan_ortu': forms.Select(
                attrs = {
                    'class':'form-control col-sm-2',
                }
            ),
        }
