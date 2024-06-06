from django.db import models
from models_package.models.user import MyUserLibModel
from models_package.models.flight import FlightLibModel

class BookingLibModel(models.Model):
    flight = models.ForeignKey(FlightLibModel, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(MyUserLibModel, related_name='bookings', on_delete=models.CASCADE)
    number = models.AutoField(primary_key=True)
    amount = models.PositiveSmallIntegerField(default=1)
    price = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = (
        ("В обработке", "В обработке"),
        ("Принят", "Принят"),
        ("Отменён", "Отменён"),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Принят")
    
    class Meta:
        app_label = 'models_package'
