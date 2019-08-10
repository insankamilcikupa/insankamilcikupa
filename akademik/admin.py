from django.contrib import admin

# Register your models here.

from .models import Siswa
from .models import Guru


class SiswaAdmin(admin.ModelAdmin):
    readonly_fields = [
                        'slug',
                        'waktuEdit',
    ]

admin.site.register(Siswa,SiswaAdmin)
admin.site.register(Guru)
