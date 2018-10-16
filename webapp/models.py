# -*- coding: utf-8 -*-
from django.db import models

class airQuality(models.Model):
    valor = models.IntegerField()
    variable = models.CharField(max_length = 100,null=True)
    fecha =  models.DateTimeField(blank=True, null=True)


   # def save(self):
    #    self.id = airQuality.objects.count()+1
     #   super(airQuality, self).save()