from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    pass

    def __unicode__(self):
        return self.name


