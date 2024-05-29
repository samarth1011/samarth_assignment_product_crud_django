from django.db import models

# Create your models here.
class Product(models.Model):
    # it takes by default this autofield
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    category = models.CharField(max_length=255)
    price = models.FloatField()
 
    def __str__(self) -> str:
        return self.name
    

