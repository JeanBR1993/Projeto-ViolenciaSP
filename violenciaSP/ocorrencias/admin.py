from django.contrib import admin
from .models import Delegacia, Crime, DadosBoletim, Mes

# Register your models here.

admin.site.register(Delegacia)
admin.site.register(Crime)
admin.site.register(DadosBoletim)
admin.site.register(Mes)
