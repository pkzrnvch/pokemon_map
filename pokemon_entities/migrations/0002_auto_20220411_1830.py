# Generated by Django 3.1.14 on 2022-04-11 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='defence',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='health',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='level',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='stamina',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='strength',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
