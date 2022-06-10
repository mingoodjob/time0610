from django.db import models

class UserModel(models.Model):
    class Meta:
        db_table = "user"

    email = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    