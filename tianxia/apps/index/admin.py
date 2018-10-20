from django.contrib import admin
from .import models
# Register your models here.

class show_pictures_index_admin(admin.ModelAdmin):
    list_display = ['id','description','picture']

class Book_admin(admin.ModelAdmin):
    list_display = ['id','author']
    inlines = [models.Book_colomn_details]

class Book_colomn_details_admin(admin.ModelAdmin):
    ordering = ['book','create_time']

admin.site.register(models.show_pictures_index,show_pictures_index_admin)
admin.site.register(models.Book)
admin.site.register(models.Book_colomn_details,Book_colomn_details_admin)
