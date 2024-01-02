from django.db import models


class UserProfile(models.Model):
    user_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.phone_number}'


class Account(models.Model):
    phone_number = models.CharField(max_length=20, unique=True)
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='account')
