from django.conf.urls.defaults import *
from photos.views import *

urlpatterns = patterns('',

	# /photos/all shows all the photos
    url(r'^all$',
        view = AllPhotos.as_view(),
        name = 'all_photos'
    ),

    # /photos/id# shows an individual photo
    url(r'^(?P<pk>\d+)$',
        view = PhotoDetail.as_view(),
        name = 'photo_detail'
    ),

)