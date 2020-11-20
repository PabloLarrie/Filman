from embed_video.fields import EmbedVideoField
from django.db import models


class pelicula(models.Model):
    titulo=models.CharField(max_length=40)
    portada=models.ImageField(upload_to='films')
    agno=models.DateField()
    actores=models.TextField()
    trailer=EmbedVideoField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    fav=models.BooleanField(default=False)
    
    

    class Meta:
        verbose_name= 'pelicula'
        verbose_name_plural= 'peliculas'
    
    def __str__(self):
        return self.titulo


