from django.db import models


class Airport(models.Model): 
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f"{self.city}, {self.code}"
        
# Create your models here.
class Flights(models.Model):
    __tablename__ = "flights"

    #origin = models.CharField(max_length=64)
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    #destination = models.CharField(max_length=64)
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.id}: {self.origin} to {self.destination} for {self.duration}"
