from django.db import models
from django.forms import CharField, DateField

# Create your models here.

# Class for the users of this system.
class user(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)

    def __str__(self):
        r_user ="{0}, {1} - [{2}]"
        return r_user.format(self.last_name, self.first_name, self.role) 
         
# Class for the memebers of the Gym
class member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    id_card = models.CharField(max_length=8, unique=True, default=00000000)
    phone = models.CharField(max_length=13)

    def __str__(self):
        r_member = "{0}, {1} ({2})"
        return r_member.format(self.last_name, self.first_name, self.id_card)

# Class for the staff of the gym
class staff(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        r_staff = "{0}, {1}"
        return r_staff.format(self.last_name, self.first_name)

# Class for the training/classes available in the Gym.
class training(models.Model):
    code = models.SmallIntegerField(default=00000)
    name = models.CharField(max_length=255)

    def __str__(self):
        r_training = "{0} ({1})"
        return r_training.format(self.name, self.code)