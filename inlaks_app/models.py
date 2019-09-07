from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
# Create your models here.

status_ = [
    ('Success', 'Success'),
    ('Failed', 'Failed'),
    ('Reversed', 'Reversed')
]


class ATM(models.Model):
    pan_number = models.IntegerField(validators=[RegexValidator(regex='^.{19}$', message='Length has to be 19', code='nomatch')], unique=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    location = models.TextField()
    acc_num = models.IntegerField(validators=[RegexValidator(regex='^.{10}$', message='Length has to be 10', code='nomatch')], unique=True)
    date_of_transaction = models.DateTimeField(default=timezone.now)
    atm_or_pos = models.BooleanField(choices=[(True, 'ATM'),(False, "POS")])
    status = models.CharField(choices=status_, default='Success', max_length=8)

    def __str__(self):
        return f'{self.amount} at {self.location}'



class Service(models.Model):
    name = models.CharField(max_length=50)
    is_online = models.BooleanField()

    def __str__(self):
        return self.name


    #>>> ATM.objects.filter(date_of_transaction__day=day)
