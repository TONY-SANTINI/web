from django.contrib import admin
from compunet.models import *

# Register your models here.
class DistribuidorAdmin(admin.ModelAdmin):
    list_display=('nombre','direccion','telefono','email',)
    search_fields=('nombre','telefono',)

class ProducoAdmin(admin.ModelAdmin):
    list_display=('nombre','marca','tipo','precio',)
    search_fields=('nombre','marca',)
    list_filter=('nombre','marca','tipo','precio',)
    ordering=('-nombre',)



admin.site.register(Distribuidor)
admin.site.register(Producto)