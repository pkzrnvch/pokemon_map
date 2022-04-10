from django.db import models  # noqa F401

class Pokemon(models.Model):
    """Покемон."""
    title = models.CharField('Название', max_length=200)
    image = models.ImageField('Картинка', upload_to='pokemon_images', null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')
    appeared_at = models.DateTimeField('Время появления', null=True, blank=True)
    disappeared_at = models.DateTimeField('Время исчезновения', null=True, blank=True)
