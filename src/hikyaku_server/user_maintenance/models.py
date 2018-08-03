from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    mail = models.EmailField()
    password = models.CharField(max_length=50)
    point = models.IntegerField(default=0)
    note = models.TextField()

    def __repr__(self):
        return "{}: {}".format(self.pk, self.name)

    __str__ = __repr__

