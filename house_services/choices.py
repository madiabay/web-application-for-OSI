from django.db import models

class NoteTypeChoices(models.TextChoices):
    New = 'New'
    InProcess = 'InProcess'
    Done = 'Done' 