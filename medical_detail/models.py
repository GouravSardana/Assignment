from django.db import models

class Disease(models.Model):
    name = models.CharField(max_length=30)
    symptoms = models.TextField(max_length=500)
    causes = models.TextField(max_length=500)
    diagnosis = models.TextField(max_length=500)
    treatment = models.TextField(max_length=500)
    prevention = models.TextField(max_length=500)

    def __str__(self):
        return self.name
