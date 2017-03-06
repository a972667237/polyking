from django.db import models

class Things(models.Model):
    thing_text = models.CharField(max_length=200)
    add_date = models.DateTimeField('date published', auto_now=True)
    def __str__(self):
        return self.thing_text
