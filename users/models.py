from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):

    class Meta:
        verbose_name = 'Utilisateurs'
        verbose_name_plural = 'Utilisateurs'

    def __str__(self):
        return "id:{}, username:{}".format(self.id, self.username)
