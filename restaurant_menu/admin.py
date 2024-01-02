from django.contrib import admin
from .models import Item

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("meal","status")
    list_filter = ("status",)
    search_fields = ("meat","description")


admin.site.register(Item,MenuItemAdmin)

# pycharm manage.py runserver   --- on termianl
# username: sanju   password:sanju
# email:sanjanaarj2003@gmail.com
#http://127.0.0.1:8000/admin    ---- in webpage(edge)