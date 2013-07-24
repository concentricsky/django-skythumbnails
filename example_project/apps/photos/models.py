from django.db import models
from sky_thumbnails.fields import EnhancedImageField

# A simple photo model with title, description, and image fields
class Photo(models.Model):
	title = models.CharField(
		max_length = 200,
		help_text = 'Title of the image',
	)
	description = models.CharField(
		max_length = 500,
		help_text = 'Description of the image',
	)
	# The EnhancedImageField will upload the photo into the uploads
	# directory at the indicated resolution when you save the file.
	# Smaller sizes (thumbnails) will be generated on-demand in the
	# uploads/thumbnails directory.
	image = EnhancedImageField(
        verbose_name='Image of various sizes',
        upload_to = 'uploads',

        # (width, height) of original image. The image will be cropped
        # if it does not match the indicated dimensions
        process_source = dict(size=(300,300)),
        
        thumbnails = {
        	# identifier for the size (can be anything you choose), again
        	# with the (width, height).
            'medium': dict(size=(115,115)),
            'small': dict(size=(80,80)),
            'icon': dict(size=(30,30)),
        }
    )