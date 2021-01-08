from django.contrib import admin
from .models import NoSlugTest, SlugTest
# Register your models here.



admin.site.register(NoSlugTest)
admin.site.register(SlugTest)