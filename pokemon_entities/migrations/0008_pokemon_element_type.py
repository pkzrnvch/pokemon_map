# Generated by Django 3.1.14 on 2022-04-12 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0007_pokemonelementtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='element_type',
            field=models.ManyToManyField(blank=True, to='pokemon_entities.PokemonElementType', verbose_name='Стихия'),
        ),
    ]
