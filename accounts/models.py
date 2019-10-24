# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Feedback(models.Model):
    customer_name = models.CharField(max_length=120)
    feedback = models.TextField()
    date = models.DateField(auto_now_add=True)
