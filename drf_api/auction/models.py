from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class User(models.Model):
    username = models.CharField(max_length=255)
    balance = models.IntegerField(default=0)
    deleted = models.BooleanField(default=False)


class Item(models.Model):

    class Kind(models.TextChoices):
        CAT = 'cat', 'Cat'
        HEDGEHOG = 'hedgehog', 'Hedgehog'
        OTHER = 'other', 'Other'

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    kind = models.CharField(
        max_length=32, choices=Kind.choices, default=Kind.OTHER
    )
    deleted = models.BooleanField(default=False)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    good_id = models.PositiveIntegerField()
    good = GenericForeignKey('content_type', 'good_id')


class Cat(models.Model):
    breed = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)


class Hedgehog(models.Model):
    breed = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)


class Lot(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Bid(models.Model):
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
