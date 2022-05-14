from django.contrib import admin
from django.urls import path

from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    
	path('account/', include(('myAccount.urls', 'myAccount'), namespace='myAccount')),
    path('api/v1/account/', include(('restAccount.urls', 'restprofile'), namespace='restAccount')),
]