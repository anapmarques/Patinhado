from django.contrib import admin

# Register your models here.
from PatinhadoWeb.models import Usuario, Pet, PedidoAdocao

admin.site.register(Usuario)
admin.site.register(Pet)
admin.site.register(PedidoAdocao)