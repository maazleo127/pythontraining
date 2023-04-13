from django.contrib import admin

from .models import User , Auction , Bids

admin.site.register(User)
admin.site.register(Auction)
admin.site.register(Bids)


# Register your models here.
