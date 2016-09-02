# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from slughifi import slughifi

# Create your models here.

class Group(models.Model):
	name = models.CharField(max_length=64)

	def __unicode__(self):
		return self.name

class Spell(models.Model):
	name = models.CharField(max_length=64)
	slug = models.SlugField(max_length=100, editable=False)
	description = models.TextField()
	group = models.ForeignKey(Group)
	range = models.CharField(max_length=64, blank=True)

	type_choices = (
		('e', 'Efecto'),
		('r', 'Rayo'),
		('i', 'Invocación'),
	)

	type = models.CharField(max_length=1, choices=type_choices, default='e')

	def save(self, *args, **kwargs):
		self.slug = slughifi(self.name)
		super(Spell, self).save(*args, **kwargs)

