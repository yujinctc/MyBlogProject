from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.db import models

# Create your models here.
from django.utils.translation import ugettext_lazy


class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)

    username_validator = ASCIIUsernameValidator()

    email = models.EmailField(ugettext_lazy('email address'), blank=True, unique=True)

    class Meta(AbstractUser.Meta):
        pass

# 另一种完善User模型的方式。
# class Profile(models.Model):
#     nickname = models.CharField(max_length=50, blank=True)
#     user = models.OneToOneField(User)
