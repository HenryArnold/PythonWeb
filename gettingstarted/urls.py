from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
admin.autodiscover()

import hello.views
import logs.views
import poem.views
# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^help', hello.views.help, name='help'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^google740430dd129e0ed2', hello.views.google, name='google'),
    path('logs/', logs.views.logs),
    path('poem/', poem.views.poem),
    path('admin/', admin.site.urls),
]
