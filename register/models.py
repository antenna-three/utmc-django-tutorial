from django.db import models

# Create your models here.
class Entry(models.Model):
    def __str__(self):
        return self.screen_name

    screen_name = models.CharField(max_length=100)
    admission_year = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
