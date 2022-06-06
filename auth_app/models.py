from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomManager(BaseUserManager):
    def create_user(self, email, password, **other_fields):

        email = self.normalize_email(email)

        user = self.model(email=email, **other_fields)
        user.set_password(password)

        if user.is_superuser is True:
            user.role = 'AD'
        else:
            user.role = 'US'
        user.save()
        return user

    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('role', 'AD')

        if other_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff = true')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser = true')
        if other_fields.get('is_active', True) is not True:
            raise ValueError('Суперпользователь должен иметь is_active = true')

        return self.create_user(email, password, **other_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    ADMIN = 'AD'
    USER = 'US'
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (USER, "User"),
    ]
    email = models.EmailField(unique=True, verbose_name='Почта пользователя')

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    role = models.CharField(max_length=2, verbose_name='Роль', choices=ROLE_CHOICES, default=USER)

    objects = CustomManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.email} - {self.role}'


class Posts(models.Model):

    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание поста')
    is_public = models.BooleanField(default=True, verbose_name='Публичный пост')


    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.name

