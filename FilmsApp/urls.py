from django.urls import path
from FilmsApp import views
from django.conf import settings
from django.conf.urls.static import static
from .views import filmsdef

urlpatterns = [
    path('films/', views.filmsdef, name="Films"),
]



#urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)