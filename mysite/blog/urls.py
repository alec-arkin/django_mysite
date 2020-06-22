from django.urls import path
from mysite.blog.views import archive

urlpatterns = [
     path('', archive),
]
