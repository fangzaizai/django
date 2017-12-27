# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Moment(models.Model):
	content=models.CharField(max_length=200)
	user_name=models.CharFiled(max_length=200)
	kind=models.CharFiled(max_length=20)