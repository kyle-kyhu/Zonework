from django.contrib import admin
from .models import Student, Item, LearningItem

admin.site.register(Student)
admin.site.register(Item)
admin.site.register(LearningItem)

