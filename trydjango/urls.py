from django.conf.urls import url, include
from django.contrib import admin

from todo import urls as todo_urls
from comments import urls as comments_urls

import home.views as home_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_views.get_index, name="home"),
    url(r'^chat/', include(comments_urls)),
    url(r'^todo/', include(todo_urls)),
]