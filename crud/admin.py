from django.contrib import admin
from crud.models import member, staff, training, user

# Register your models here.

admin.site.register(user)
admin.site.register(member)
admin.site.register(staff)
admin.site.register(training)