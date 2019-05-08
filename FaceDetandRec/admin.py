from django.contrib import admin
from .models import User, OriPic, TarPic, Record

# Register your models here.


admin.site.register(User)
admin.site.register(OriPic)
admin.site.register(TarPic)
admin.site.register(Record)

