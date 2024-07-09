from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Car(models.Model):
    title = models.CharField(max_length=30, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'автомобиль'
        verbose_name_plural = 'автомобили'


class Moto(models.Model):
    title = models.CharField(max_length=30, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'мотоцикл'
        verbose_name_plural = 'мотоциклы'


class Milage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='машина', **NULLABLE)
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, verbose_name='мотоцикл', **NULLABLE)
    milage = models.PositiveIntegerField(verbose_name='пробег в км')
    year = models.PositiveSmallIntegerField(verbose_name='год регистрации')

    def __str__(self):
        return f'{self.milage} км - {self.year} год'

    class Meta:
        verbose_name = 'пробег'
        verbose_name_plural = 'пробеги'
        ordering = ('-year',)