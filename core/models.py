from django.db import models
from django.contrib.auth.models import User

class Batch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    batch_label = models.CharField(max_length=100)
    variety = models.CharField(max_length=100)
    inoculation_date = models.DateField()
    num_bags = models.IntegerField()
    contaminated_bags = models.IntegerField(default=0)
    notes = models.TextField(blank=True, null=True)
    stage = models.CharField(max_length=50, default='incubation')
    grow_room_entry_date = models.DateField(blank=True, null=True)
    retirement_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.batch_label} - {self.variety}"
