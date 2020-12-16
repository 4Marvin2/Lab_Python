from django.db import models


class Processor(models.Model):
    name = models.CharField(max_length=20)


class Description(models.Model):
    processor_id = models.ForeignKey(Processor, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
