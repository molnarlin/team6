from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category

@admin.register(Category)
class CategoryAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)  # Enable Summernote for the description field
    list_display = ('name',)  # Display the name in the admin list view