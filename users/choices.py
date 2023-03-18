from django.db import models


class UserTypeChoices(models.TextChoices):
    Liver = 'Liver'
    Chairman = 'Chairman'
    # Admin = 'Admin'