from django.db import models  # noqa F401

class Pokemon(models.Model):
    """Покемон."""
    title = models.CharField('Название', max_length=200)
    image = models.ImageField('Картинка', upload_to='pokemon_images', null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

class PokemonEntity(models.Model):
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')
