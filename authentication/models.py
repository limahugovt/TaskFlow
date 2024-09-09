from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone

class UserManager(BaseUserManager):
  def create_user(self, name, email, password=None, **extra_fields):
    if name is None:
      raise ValueError('User must provide a name')
    if email is None:
      raise ValueError('User must provide an email')

    user = self.model(name=name, email=self.normalize_email(email), **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, name, email, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)

    if extra_fields.get('is_staff') is not True:
      raise ValueError('O superusuário precisa ter is_staff=True.')
    if extra_fields.get('is_superuser') is not True:
      raise ValueError('O superusuário precisa ter is_superuser=True.')

    return self.create_user(name=name, email=email, password=password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
  user_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  email = models.EmailField(max_length=255, unique=True)
  password = models.CharField(max_length=255)
  is_superuser = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)
  is_admin = models.BooleanField(default=False)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['name']

  objects = UserManager()

  def __str__(self):
    return self.name

class Board(models.Model):
  board_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  description = models.TextField()
  created_at = models.DateTimeField(default=timezone.now)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

class List(models.Model):
  list_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  description = models.TextField()
  order = models.IntegerField()
  board = models.ForeignKey(Board, on_delete=models.CASCADE)

class EpicLink(models.Model):
  epic_link_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  description = models.TextField()

  def __str__(self):
    return self.name

class Card(models.Model):
  PRIORITY_CHOICES = [
    (0, 'Normal'),
    (1, 'Moderado'),
    (2, 'Alto'),
    (3, 'Muito Alto')
  ]
  card_id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=255)
  description = models.TextField()
  creation_date = models.DateTimeField(default=timezone.now)
  delivery_date = models.DateTimeField(null=True, blank=True)
  priority = models.IntegerField(default=0, choices=PRIORITY_CHOICES)
  epic_link = models.ForeignKey(EpicLink, on_delete=models.CASCADE, null=True, blank=True)
  list = models.ForeignKey(List, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title
  
  def get_priority_display(self):
    return dict(self.PRIORITY_CHOICES)[self.priority]
  

class MemberCard(models.Model):
  card = models.ForeignKey(Card, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  class Meta:
    unique_together = ('card', 'user')

class Comment(models.Model):
  comment_id = models.AutoField(primary_key=True)
  content = models.TextField()
  comment_date = models.DateTimeField(default=timezone.now)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  card = models.ForeignKey(Card, on_delete=models.CASCADE)

class Attachment(models.Model):
  attachment_id = models.AutoField(primary_key=True)
  file_name = models.CharField(max_length=255)
  file_url = models.URLField()
  upload_date = models.DateTimeField(default=timezone.now)
  card = models.ForeignKey(Card, on_delete=models.CASCADE)

