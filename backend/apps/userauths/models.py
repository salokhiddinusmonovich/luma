from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100)

    def __str__(self):
        return self.name
    

class User(AbstractUser):
    """
    Custom user model for Luma platform
    """

    # Authentication 
    email = models.EmailField(unique=True) # Used as the login field 
    username = models.CharField(unique=True, max_length=50)
    fullname = models.CharField(max_length=50, null=True, blank=True)
    google_id = models.CharField(max_length=500, unique=True, null=True, blank=True)
    avatar = models.CharField(max_length=500, unique=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    # Profile/Account details 
    bio = models.TextField(null=True, blank=True)
    website = models.CharField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=20, blank=True, null=True,choices=[('male', 'Male'), ('female', 'Female')])
    birthdate = models.DateField(null=True, blank=True)

    # Status (denormalized for speed)
    followers_count = models.PositiveIntegerField(default=0)
    following_count = models.PositiveIntegerField(default=0)
    likes_received = models.PositiveIntegerField(default=0) # total likes across all videos

    # Platform feature 
    is_verified = models.BooleanField(default=False)
    is_created = models.BooleanField(default=False) # show badge or access extra feature 
    is_private = models.BooleanField(default=False) # if account is locked/private

    last_seen = models.DateTimeField(default=timezone.now)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')

class UserCoinBalance(models.Model):
    """
    Model to store the total coin balance for each user.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='coin_balance')
    total_coin = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}`s Balance: {self.total_coin} coins"
    
    class Meta:
        verbose_name = "User Coin Balance"
        verbose_name_plural = "User Coin Balances"


class CoinPurchaseHistory(models.Model):
    """
    Model to log every coin purchase transaction for history records.
    """

    PAYMENT_METHOD_CHOICES = [
        ('payme', 'Payme'),
        ('click', 'Click')
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="purchase_history")
    coins_purchased = models.PositiveIntegerField()
    price = models.PositiveIntegerField(help_text="Price in SUM")
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES)
    transaction_id = models