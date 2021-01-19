


# Create your models here.

###########################################
# You have to write the code in settings.py AUTH_USER_MODEL = 'App_Login.User'
# Before running python manage.py  migrate command create this model
# After creating this model run
# 1. python manage.py makemigrations App_Login
# 2. python manage.py  migrate
# 3. python manage.py  createsuperuser.


#     It will ask email address





# Do not run migration or create superuser before creating this model






###########################################



from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import ugettext_lazy

# To Automatically create one to one objects
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class MyUserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError("The Email Must be Set")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser Must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=False)

# New field in User model can be added here
#     user_choice= (
#         ('Patient','Patient'),
#         ('Doctor', 'Doctor')
#     )

    # user_type=models.CharField(max_length=15, choices=user_choice)

    username = models.CharField(max_length=264, null=True, blank=True)
    full_name = models.CharField(max_length=264, null=True, blank=True)
    # designation = models.CharField(max_length=264, null=True, blank=True)
    address_1 = models.TextField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=40, null=True, blank=True)
    zipcode = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    # healthcard = models.CharField(max_length=20, blank=True, null=True)
    date_of_join = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='profile', default='no-name.jpg', null=True)

    is_staff = models.BooleanField(
        ugettext_lazy('Staff'), default=False,
        help_text=ugettext_lazy('Designates whether the user can log in the site')
    )

    is_active = models.BooleanField(
        ugettext_lazy('active'),
        default=True,
        help_text=ugettext_lazy('Designates whether this user should be treatea as active')
    )

    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email


class Coupon(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='coupon')
    couponId = models.CharField(max_length=15)
    amount = models.DecimalField(default=0.0,decimal_places=2,max_digits=6)
    transaction = models.BooleanField(default=False)
    used = models.BooleanField(default=False)



    def __str__(self):
        return self.user.email

    # def is_fully_filled(self):
    #     fields_name = [f.name for f in self._meta.get_fields()]
    #
    #     for field_name in fields_name:
    #         value = getattr(self, field_name)
    #         if value is None or value == '':
    #             return False
    #     return True


@receiver(post_save, sender=User)
def create_coupon(sender, instance, created, **kwargs):
    if created:
        Coupon.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_coupon(sender, instance, **kwargs):
    instance.coupon.save()
