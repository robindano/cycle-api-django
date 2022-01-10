from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Gift(models.Model):
    giver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gifts_given')
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='gifts_won')
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True)
    description = models.CharField(max_length=500)
    category = models.CharField(max_length=30)
    condition = models.CharField(max_length=30)
    active = models.BooleanField(default=True)
    interested_users = models.ManyToManyField(User, blank=True, related_name='gifts_interested')
    created = models.DateTimeField(auto_now_add=True)
    hours_active = models.IntegerField(blank=True, default=24)