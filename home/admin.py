from django.contrib import admin
from . import models


@admin.register(models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')


@admin.register(models.Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


@admin.register(models.FeedBackHome)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'description')

# admin.site.register(models.Lesson)
# admin.site.register(models.Teacher)
# admin.site.register(models.Price)
