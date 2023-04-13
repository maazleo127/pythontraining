from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group


class User(AbstractUser):
    phone= models.IntegerField
    address=models.CharField(max_length=256)
    groups = models.ManyToManyField(Group, related_name='auction_users')


class Auction(models.Model):
    title=models.CharField(max_length=25)
    description=models.TextField
    current_bid=models.IntegerField(null=False,blank=False)
    groups = models.ManyToManyField(Group, related_name='auction_users')


class Bids(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    new_bid = models.DecimalField(max_digits=8, decimal_places=2)
    done_at = models.DateTimeField(auto_now_add=True)
    groups = models.ManyToManyField(Group, related_name='auction_users')

# class Poll(models.Model):
#     question = models.CharField(max_length=100)
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE)
#     pub_date = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.question


# class Choice(models.Model):
#     poll = models.ForeignKey(Poll, related_name='choices', on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=100)

#     def __str__(self):
#         return self.choice_text


# class Vote(models.Model):
#     choice = models.ForeignKey(Choice, related_name='votes', on_delete=models.CASCADE)
#     poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
#     voted_by = models.ForeignKey(User, on_delete=models.CASCADE)

#     class Meta:
#         unique_together = ("poll", "voted_by")

# Create your models here.
