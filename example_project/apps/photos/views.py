from django.views.generic import *
from photos.models import Photo

# /photos/all shows all the photos
class AllPhotos(ListView):
	model = Photo
	template_name = 'allphotos.html'

# /photos/id# shows an individual photo
class PhotoDetail(DetailView):
	model = Photo
	template_name = 'photodetail.html'