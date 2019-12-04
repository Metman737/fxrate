from django.contrib.auth.models import User
from django.db import models

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts') # Das Löschen muss getestet werden.
    short_description = models.TextField(max_length=150)
    content = models.TextField()
    img = models.ImageField()
    category = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, )

    class Meta:
        ordering = ['creation_date']

    def __str__(self):
        return self.title


class Currency(models.Model):
    name = models.CharField(max_length=50, unique=True)
    token = models.CharField(max_length=5, unique=True)
    symbol = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.name


class ExchangeRate(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='currency')
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    change = models.DecimalField(max_digits=6, decimal_places=2)
    change_date = models.DateField(auto_now_add=True)
    change_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.currency.name

  #  EURO€ =
    #POUND£
    #INDIAN Rs.
   # PAKISTAN Rs.
    #IRAN Toman
    #CNY¥
   # UAE DIRHAM
    #SAUDI RIYAL