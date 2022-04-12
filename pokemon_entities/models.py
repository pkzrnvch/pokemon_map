from django.db import models  # noqa F401

class Pokemon(models.Model):
    """Покемон."""
    title = models.CharField('Название', max_length=200)
    title_en = models.CharField(blank=True, max_length=200)
    title_jp = models.CharField(blank=True, max_length=200)
    image = models.ImageField('Картинка', upload_to='pokemon_images', null=True, blank=True)
    description = models.TextField(blank=True)
    previous_evolution = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='next_evolutions',
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return f'{self.title}'

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField(null=True, blank=True)
    disappeared_at = models.DateTimeField(null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)
    health = models.IntegerField(null=True, blank=True)
    strength = models.IntegerField(null=True, blank=True)
    defence = models.IntegerField(null=True, blank=True)
    stamina = models.IntegerField(null=True, blank=True)
