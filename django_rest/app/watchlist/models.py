from django.core.validators import (MinValueValidator, MaxValueValidator)
from django.db import models


class StreamPlatform(models.Model):
    name = models.CharField(max_length=39)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.website}'


class WatchList(models.Model):
    name = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    platform = models.ForeignKey(to='watchlist.StreamPlatform', on_delete=models.DO_NOTHING,
                                 related_name='watchlist')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.storyline}'


class Reviews(models.Model):
    watchlist = models.ForeignKey('watchlist.WatchList', on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'reviews'

    def __str__(self):
        return f'{self.watchlist} | {self.rating}'
