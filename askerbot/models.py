from django.db import models


class Contact(models.Model):
    telegram_id = models.IntegerField(primary_key=True)
    phone = models.CharField(max_length=16, null=True)
    
    def __str__(self):
        return f"ID:{self.telegram_id}"
