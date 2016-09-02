# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from slughifi import slughifi

# Create your models here.

class Type(models.Model):
	name = models.CharField(max_length=64)

	def __unicode__(self):
		return self.name

class Spell(models.Model):
	name = models.CharField(max_length=64)
	slug = models.SlugField(max_length=100)
	description = models.TextField()
	type = models.ForeignKey(Type)
	range = models.CharField(max_length=64, blank=True)

	def save(self, *args, **kwargs):
		self.slug = slughifi(self.name)
		super(Spell, self).save(*args, **kwargs)

