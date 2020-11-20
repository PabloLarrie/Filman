from django.contrib import admin
from .models import pelicula
from embed_video.admin import AdminVideoMixin



class peliculaAdmin(AdminVideoMixin, admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(pelicula, peliculaAdmin)
