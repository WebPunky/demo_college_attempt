from django.db import models

class Services(models.Model):
    title = models.CharField(blank=True, max_length=30)
    desc = models.TextField(blank=True)
    image = models.ImageField(
        upload_to="services/%Y/%m/",
        blank=True,
        null=True
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.title