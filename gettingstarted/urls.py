from django.conf.urls import include, url
from django.urls import path, include

from cliente.urls import routerCliente
from django.contrib import admin
admin.autodiscover()


# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^', include('promotions.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^usuarios/', include(routerCliente.urls)),
    url(r'^admin/', admin.site.urls),
]
