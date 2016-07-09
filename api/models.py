from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models.query import Prefetch

from rest_framework.authtoken.models import Token


class UserManager(BaseUserManager):

    def create_user(self, email, password=None):

        if not email:
            raise ValueError("User must have an email")

        user = self.model(
            # email=self.normalize_email(email),
            email=email,
            is_active=True)
        user.set_password(password)
        user.save(using=self._db)
        token = Token.objects.create(user=user)
        return user, token.key

    def create_superuser(self, email, password):

        if not (email or password):
            raise ValueError("Super user must have an email and password")

        user = self.create_user(email, password)
        user.is_admin = True
        user.save()


class User(AbstractBaseUser):

    def get_full_name(self):
        pass

    def get_short_name(self):
        pass

    class Meta:
        db_table = 'users'
        managed = True

    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_verify = models.BooleanField(default=False)
    is_searchable = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __unicode__(self):
        return self.email


class UserVerification(models.Model):

    class Meta:
        db_table = 'user_verification'

    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField()

    def __unicode__(self):
        return self.email


class UserResetPassword(models.Model):

    class Meta:
        db_table = 'user_reset_password'

    user = models.OneToOneField(User)
    is_valid_key = models.BooleanField(default=False)
    key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField()

    def __unicode__(self):
        return self.email


class Post(models.Model):
    class Meta:
        db_table = 'posts'

    title = models.CharField(max_length=50, null=True)
    text = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)


class Comment(models.Model):
    class Meta:
        db_table = 'comments'

    text = models.CharField(max_length=200, null=True)
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

