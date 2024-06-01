from django.db import models

# Create your models here.

# -------- NEW STUFF -------------------------
class ToDo(models.Model):
    task = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task
# -------- NEW STUFF -------------------------
