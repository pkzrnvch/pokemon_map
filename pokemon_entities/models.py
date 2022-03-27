from django.db import models  # noqa F401

class Pokemon(models.Model):
    """Покемон."""
    title = models.CharField('Название', max_length=200)
