
from django.contrib import admin
from django.urls import path
from mainapp.views import home,report,signin,vote_count,blank

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('report/',report,name='report'),
    path('login/',signin,name='login'),
    path('vote-count/',vote_count,name='vote-count'),
    path('blank/',blank,name='blank')
]
