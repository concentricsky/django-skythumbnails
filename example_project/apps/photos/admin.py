from django.contrib import admin
from photos.models import *

# For displaying the uploaded photos in the admin site
class PhotoAdmin(admin.ModelAdmin):
	list_display = ('title', 'description', 'image')

admin.site.register(Photo, PhotoAdmin)