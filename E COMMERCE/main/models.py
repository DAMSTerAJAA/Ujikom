from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Product(models.Model):
    CATEGORY = (
        ("assaultrifle", "Assault Rifle"),
        ("sniper", "Sniper Rifle"),
        ("machinegun", "Machine Gun"),
        ("grenadelauncher", "Grenade Launcher"),
        ("mortir", "Mortir"),
        ("pistol", "Pistol"),
        ("shotgun", "Shotgun"),
        ("submachinegun", "Submachine Gun"),
        ("homemadeexplosive", "Hommade Explosive Part"),
    )
    name = models.CharField(max_length=255, null=False, blank=False)
    price = models.DecimalField(max_digits=12, decimal_places=3, null=False, blank=False)
    image_url = models.ImageField(upload_to="gambar/")
    category = models.CharField(max_length=255, choices=CATEGORY, blank=False)
    stock = models.IntegerField()
    slug = models.SlugField(default="", unique=True, blank=True)

    class order (models.Model):
         id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
         total_price = models.DecimalField(max_digits=10, decimal_places=2)
         created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name     
    
class Transaction(models.Model):
    order_id = models.CharField(max_length=255, null=False, blank=False)
    customer = models.CharField(max_length=255, null=False, blank=False)
    payment_type = models.CharField(max_length=255, null=False, blank=False)
    status = models.CharField(max_length=255, null=False, blank=False)