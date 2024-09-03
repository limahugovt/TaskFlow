from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone

class UserManager(BaseUserManager):
  def create_user(self, username, email, password=None):
    if username is None:
      raise ValueError('User must provide a name')
    if email is None:
      raise ValueError('User must provide an email')

    user = self.model(username=username, email=self.normalize_email(email))
    user.set_password(password)
    user.save(using=self._db)
    return user

class User(AbstractBaseUser):
  user_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  email = models.EmailField(max_length=255, unique=True)
  password = models.CharField(max_length=255)
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['name']

  objects = UserManager()

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

class Card(models.Model):
  card_id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=255)
  description = models.TextField()
  creation_date = models.DateTimeField(default=timezone.now)
  delivery_date = models.DateTimeField(null=True, blank=True)
  list = models.ForeignKey(List, on_delete=models.CASCADE)

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
