"""familytree URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from family import views
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^treeedit_database/(\d+)/', views.treeedit_database, name='treeedit_database'),
    url('admin/', admin.site.urls),
    url(r'^$',views.tree,name='tree'),
    url(r'^tree/(\d+)/',views.home,name='home'),
    url(r'^family/(\d+)/',views.fam_detail,name = 'fam_detail'),
    url(r'^newedit',views.newedit,name='newedit'),
    url(r'^new',views.new,name='new'),
    url(r'^childentry',views.childentry,name='childentry'),
    url(r'^authenticate',views.authenticate,name = 'authenticate'),
    url(r'^acknowledgement', views.acknowledgement, name='acknowledgement'),
    url(r'editfamily/(\d+)/',views.edit_database,name='edit_database'),
    url(r'edit_data',views.edit_data,name='edit_data'),
    url(r'childedit', views.childedit, name='childedit'),
    url(r'treeedit', views.treeedit, name='treeedit'),
    url(r'^connection',views.connection,name='connection'),
    url(r'^delete',views.delete,name='delete'),
    url(r'^familyentry',views.familyentry,name='familyentry'),
    url(r'^displayfamily/(\d+)/',views.displayfamily, name = 'displayfamily'),
    url(r'^display', views.display, name='display'),
    url(r'^imagesupload', views.imagesupload, name='imagesupload'),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
