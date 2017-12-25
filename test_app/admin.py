from django.contrib import admin

# Register your models here.
from models import Test


@admin.register(Test)
class AdminTest(admin.ModelAdmin):
    list_display = (
        'upl_text',
    )