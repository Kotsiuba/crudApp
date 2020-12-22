from django.db import models


class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    stars = models.IntegerField()
    description = models.CharField(max_length=200)

    class Meta:
        db_table = "hotels"


class Tour(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    hotel = models.ForeignKey(Hotel, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "tours"
