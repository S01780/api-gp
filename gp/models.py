from django.db import models

class Lead(models.Model):
    uclass = models.CharField(max_length=100)
    utype = models.CharField(max_length=100)
    uquantity = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
