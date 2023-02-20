from django.contrib import admin
from .models import Parameter,Observation,Station,FileUpload
# Register your models here.

admin.site.register(Parameter)
admin.site.register(Observation)
admin.site.register(Station)
admin.site.register(FileUpload)