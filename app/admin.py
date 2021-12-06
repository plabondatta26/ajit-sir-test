from django.contrib import admin
from .models import WriterModel, BlogModel
# Register your models here.

admin.site.register(WriterModel)
admin.site.register(BlogModel)