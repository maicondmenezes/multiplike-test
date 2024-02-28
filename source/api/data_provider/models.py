from django.db import models

class Event(models.Model):
    BOOKING = 1
    CANCELLATION = 2
    RPG_STATUS_CHOICES = (
        (BOOKING, 'Booking'),
        (CANCELLATION, 'Cancellation'),
    )

    hotel_id = models.CharField(max_length=12)
    timestamp = models.DateTimeField()
    rpg_status = models.IntegerField(choices=RPG_STATUS_CHOICES)
    room_id = models.CharField(max_length=12)
    night_of_stay = models.DateField()

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return (
            f'Event {self.id} for Room {self.room_id} in Hotel {self.hotel_id}'
        )