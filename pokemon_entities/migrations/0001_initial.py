# Generated by Django 3.1.14 on 2022-04-10 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('image', models.ImageField(blank=True, null=True, upload_to='pokemon_images', verbose_name='Картинка')),
            ],
        ),
        migrations.CreateModel(
            name='PokemonEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('appeared_at', models.DateTimeField(blank=True, null=True)),
                ('disappeared_at', models.DateTimeField(blank=True, null=True)),
                ('level', models.IntegerField()),
                ('health', models.IntegerField()),
                ('strength', models.IntegerField()),
                ('defence', models.IntegerField()),
                ('stamina', models.IntegerField()),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.pokemon')),
            ],
        ),
    ]
