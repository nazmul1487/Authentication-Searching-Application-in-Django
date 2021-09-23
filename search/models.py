from django.db import models
from authentication.models import User

# Create your models here.


class UserInput(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    inputValue = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.name + " : " + str(self.id)
