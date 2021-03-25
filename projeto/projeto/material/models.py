from django.db import models


class Material(models.Model):
    id_material = models.AutoField(primary_key=True)
    nm_material = models.CharField(max_length=200)

