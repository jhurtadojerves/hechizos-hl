# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from slughifi import slughifi

# Create your models here.

class Group(models.Model):
    name_choices = (
        ('Neutrales', 'Neutrales'),
        ('Orden del Fénix', 'Orden del Fénix'),
        ('Marca Tenebrosa', 'Marca Tenebrosa'),
        ('Libros de Hechizos', 'Libros de Hechizos'),
    )
    name = models.CharField(max_length=64, choices=name_choices, unique=True)
    slug = models.SlugField(allow_unicode=True, max_length=100, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slughifi(self.name).lower()
        super(Group, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class Range(models.Model):
    name = models.CharField(max_length=64)
    group = models.ForeignKey(Group)
    slug = models.SlugField(allow_unicode=True, max_length=100, editable=False)

    def save(self, *args, **kwargs):
        self.slug = self.slug = slughifi(self.name).lower()
        super(Range, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name



class Spell(models.Model):

    name = models.CharField(max_length=64, unique = True)
    slug = models.SlugField(allow_unicode=True, max_length=100, editable=False)
    description = models.TextField()
    range = models.ManyToManyField(Range)

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
        ('O', 'Objeto'),
    )

    type = models.CharField(max_length=2, choices=type_choices, default='e')
    method = models.CharField(max_length=1, choices=method_choices, default='V')
    object = models.CharField(max_length=1, choices=object_choices, default='V')

    def save(self, *args, **kwargs):
        self.slug = self.slug = slughifi(self.name).lower()
        super(Spell, self).save(*args, **kwargs)