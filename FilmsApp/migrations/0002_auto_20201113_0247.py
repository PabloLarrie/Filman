# Generated by Django 3.1.2 on 2020-11-13 01:47

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('FilmsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pelicula',
            options={'verbose_name': 'pelicula', 'verbose_name_plural': 'peliculas'},
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='portada',
            field=models.ImageField(upload_to='films'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='titulo',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='trailer',
            field=embed_video.fields.EmbedVideoField(),
        ),
    ]
