from django.db import models
import random
import string
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address", max_length=255, unique=True, null=True
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Voter(models.Model):
    name = models.CharField(max_length=254)
    code = models.CharField(max_length=6, null=True, unique=True)
    status = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def generate_code(self):
        words = list(string.ascii_uppercase)
        words.remove("O")
        words.remove("V")
        words.remove("W")
        words.remove("I")
        numbers = ["2", "3", "4", "5", "6", "7", "8", "9"]
        s = ""
        code_list = random.sample(words, 3) + random.sample(numbers, 3)
        self.code = s.join(code_list)

    class Meta:
        ordering = ("id",)


class Ballot(models.Model):
    voter = models.OneToOneField(Voter, on_delete=models.CASCADE, unique=True)
    pr = models.CharField(max_length=254)
    vp = models.CharField(max_length=254)
    sg = models.CharField(max_length=254)
    vs = models.CharField(max_length=254)
    tr = models.CharField(max_length=254)
    dt = models.CharField(max_length=254)
    os = models.CharField(max_length=254)
    eas = models.CharField(max_length=254)
    ers = models.CharField(max_length=254)
    ad = models.CharField(max_length=254)
    tru1 = models.CharField(max_length=254)
    tru2 = models.CharField(max_length=254)
    tru3 = models.CharField(max_length=254)

    def __str__(self):
        return self.voter.name


TITLES = (
    ("pr", "President"),
    ("vp", "Vice President"),
    ("sg", "Secretary General"),
    ("vs", "Vice Secretary General"),
    ("tr", "Treasurer"),
    ("dt", "Deputy Treasurer"),
    ("os", "Organizing Secretary"),
    ("eas", "External Relations Secretary"),
    ("ers", "Education and Research Secretary"),
    ("ad", "Auditor"),
    ("tru", "Trustees"),
)


class Candidate(models.Model):
    name = models.CharField(max_length=254, unique=True)
    title = models.CharField(choices=TITLES, max_length=5)
    count = models.PositiveIntegerField(default=0)

    def add_count(self):
        self.count += 1

    def __str__(self):
        return self.name


class VotingTime(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return str(self.start) + "--" + str(self.end)
