from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from turizm_core.models import DannieAutorizatsii

admin.site.register(DannieAutorizatsii, UserAdmin)

# Register your models here.
