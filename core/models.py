import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from core.manager import AnswerManager, UserManager


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    email = models.EmailField(
        unique=True,
        null=False,
        verbose_name="Email"
    )

    username = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        verbose_name="Username"
    )

    first_name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='First Name'
    )
    last_name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Last Name'
    )
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    is_block = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', )

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_username(self):
        return f"{self.username}"

    # TODO:  <14-05-21, coderj001> # Add redirect to return
    def get_absolute_url(self):
        slug_id = ''.join(str(self.id).split('-'))
        slug = f"{self.username}_{slug_id}"
        return f"/p/{slug[:15]}"

    def __str__(self):
        return str(self.username)


class Answer(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    Answer = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_created=True)
    answered_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="answer",
        verbose_name="Answered By"
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft'
    )

    objects = models.Manager()
    published = AnswerManager()

    class Meta:
        verbose_name = "Answere"
        verbose_name_plural = "Answeres"
        ordering = ('-created_at', '-updated_at')

    def __str__(self):
        return super(Answer, self).__str__()


class Question(models.Model):
    question = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        verbose_name="Question"
    )
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_created=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="question",
        verbose_name="Created By"
    )
    answers = models.ManyToManyField(
        Answer,
        related_name='question',
        verbose_name='Answers'
    )

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
        ordering = ('-created_at', '-updated_at')

    def __str__(self):
        if len(self.question) > 25:
            return f"{self.question[:25]}..."
        else:
            return self.question
