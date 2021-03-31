from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Link(models.Model):
    long = models.CharField('Длинная ссылка', max_length=250, default='')
    short = models.CharField('Короткая ссылка', max_length=100, default='', unique=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('profile')

    class Meta:
        def __str__(self):
            return self.short


        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'