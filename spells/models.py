# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from slughifi import slughifi

# Create your models here.

class Group(models.Model):
    name_choices = (
        ('Neutrales', 'Neutrales'),
        ('Orden del Fénix', 'Orden del Fénix'),
        ('Marca Tenebrosa', 'Marca Tenebrosa'),
        ('Libro del Aprendiz de Brujo', 'Libro del Aprendiz de Brujo'),
        ('Libro de la Fortaleza', 'Libro de la Fortaleza'),
        ('Libro de la Sangre', 'Libro de la Sangre'),
        ('Libro del Equilibrio', 'Libro del Equilibrio'),
        ('Libro del Druida', 'Libro del Druida'),
        ('Libro del Caos', 'Libro del Caos'),
        ('Libro de los Ancestros', 'Libro de los Ancestros'),
        ('Libro de las Auras', 'Libro de las Auras'),
        ('Libro de Hermes Trimegisto', 'Libro de Hermes Trimegisto'),
        ('Libro de Merlín', 'Libro de Merlín')
    )
    name = models.CharField(max_length=64, choices=name_choices, unique=True)

    def __unicode__(self):
        return self.name

class Spell(models.Model):

    name = models.CharField(max_length=64, unique = True)
    slug = models.SlugField(allow_unicode=True, max_length=100, editable=False)
    description = models.TextField()
    group = models.ManyToManyField(Group)
    range = models.CharField(max_length=64, blank=True)

    type_choices = (
        ('e', 'Efecto'),
        ('r', 'Rayo'),
        ('i', 'Invocación'),
        ('o', 'Invocación - Efecto'),
        ('ei', 'Efecto - Invocación'),
        ('eq', 'Equipable'),
        ('om', 'Onda Mágica')
    )

    method_choices = (
        ('V', 'Verbal'),
        ('N', 'No Verbal'),
    )

    object_choices = (
        ('V', 'Con Varita'),
        ('N', 'Sin Varita'),
        ('O', 'Anillo, Colgante, etc'),
    )

    type = models.CharField(max_length=2, choices=type_choices, default='e')
    method = models.CharField(max_length=1, choices=method_choices, default='V')
    object = models.CharField(max_length=1, choices=object_choices, default='V')

    def save(self, *args, **kwargs):
        self.slug = (self.name).replace(' ', '-').lower()
        super(Spell, self).save(*args, **kwargs)