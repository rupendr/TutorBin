from django.contrib import admin
from app.models import *


# Register your models here.
class GroupAdmin(admin.ModelAdmin):  # Display description Driver table me
    list_display = (
        'id', 'created_at')


admin.site.register(group, GroupAdmin)


class QuestionAdmin(admin.ModelAdmin):  # Display description Driver table me
    list_display = (
        'id', 'question', 'comment', 'created_at', 'group_id')


admin.site.register(question, QuestionAdmin)
