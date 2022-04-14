from django.db import models  # noqa F401


class PokemonElementType(models.Model):
    title = models.CharField('Стихия', max_length=200)
    image = models.ImageField(
        'Картинка',
        upload_to='pokemon_images',
        null=True,
        blank=True
    )
    strong_against = models.ManyToManyField(
        'self',
        verbose_name='Силен против',
        blank=True,
        symmetrical=False
    )

    def __str__(self):
        return self.title


class Pokemon(models.Model):
    """Покемон."""
    title = models.CharField('Название', max_length=200)
    title_en = models.CharField('Название(англ.)', blank=True, max_length=200)
    title_jp = models.CharField('Название(яп.)', blank=True, max_length=200)
    image = models.ImageField(
        'Картинка',
        upload_to='pokemon_images',
        null=True,
        blank=True
    )
    element_type = models.ManyToManyField(
        PokemonElementType,
        verbose_name='Стихия',
        blank=True
    )
    description = models.TextField('Описание', blank=True)
    previous_evolution = models.ForeignKey(
        'self',
        verbose_name='Эволюция',
        null=True,
        blank=True,
        related_name='next_evolutions',
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        verbose_name='Покемон',
        on_delete=models.CASCADE
    )
    lat = models.FloatField('Широта',)
    lon = models.FloatField('Долгота',)
    appeared_at = models.DateTimeField('Момент появления', null=True, blank=True)
    disappeared_at = models.DateTimeField('Момент исчезновения', null=True, blank=True)
    level = models.IntegerField('Уровень', null=True, blank=True)
    health = models.IntegerField('Здоровье', null=True, blank=True)
    strength = models.IntegerField('Сила', null=True, blank=True)
    defence = models.IntegerField('Защита', null=True, blank=True)
    stamina = models.IntegerField('Выносливость', null=True, blank=True)
