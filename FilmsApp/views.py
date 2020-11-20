from django.shortcuts import render, HttpResponse
from FilmsApp.models import pelicula
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

def filmsdef(request):
    peliculas=pelicula.objects.all()
    return render(request, 'FilmsApp/films.html', {"peliculas": peliculas})


@method_decorator(login_required, name='dispatch')
class filmsUpdate(UpdateView):
    form_class=pelicula
    success_url=reverse_lazy('films_signed')
    template_name='FilmsApp/films_signed.html'

    def get_object(self):
        #recuperar el objeto que se va a editar
        favs=pelicula.fav
        if favs == True:
            return favs
        else:
            pass

# Create your views here.
