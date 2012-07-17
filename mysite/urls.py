from django.conf.urls import patterns, include, url
#from piston.resource import Resource
#from piston.authentication import HttpBasicAuthentication
from djangorestframework.resources import ModelResource
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from wangxi.models import Message
from wangxi.views import ObjectStoreRoot, StoredObject
#from objectstore.views import ObjectStoreRoot, StoredObject

from djangorestframework.compat import View  
from djangorestframework.mixins import ResponseMixin  
from djangorestframework.renderers import DEFAULT_RENDERERS  
from djangorestframework.response import Response  
  
from django.core.urlresolvers import reverse  

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from django.http import HttpResponse
import os

admin.autodiscover()
#from mysite.views import wangxi

class MyResource(ModelResource):
      model = Message

class ExampleView(ResponseMixin,View):  
      renderers=DEFAULT_RENDERERS  
  
      def get(self,request):  
          response=Response(200,{'description':'Some example content',  
          'url':reverse('mixin-view')})  
          return self.render(response)
          #return HttpResponse("""'description':'Some example content','url':reverse('mixin-view')""")

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^wangxi/$', 'wangxi.views.index'),
     url(r'^djangorestframework/$', include('djangorestframework.urls')),
     #url(r'^api/$', 'api.views.index'),
     #url(r'^swift/$', include('swift_app.urls')),
     url(r'^msg/$', ListOrCreateModelView.as_view(resource=MyResource)),
     url(r'^msg/(?P<pk>[^/]+)/$', InstanceModelView.as_view(resource=MyResource)),
     
     url(r'^api$', ObjectStoreRoot.as_view(), name='object-store-root'),
     url(r'^api/(?P<key>[A-Za-z0-9_-]{1,64})/$', StoredObject.as_view(), name='stored-object'),

     url(r'^test$',ExampleView.as_view(),name='mixin-view'),  
     #url(r'^demo/$','depot.views.detail'),  
)

urlpatterns += patterns('swift_app.views',
    # Example:
    # (r'^swift_app/', include('swift_app.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/', include(admin.site.urls)),
    (r'^$','login'),
    (r'^login/$', 'login'),
    (r'^register/$','register'),
    (r'^logout/$', 'logout'),
    (r'^already-logged/$','already_logged'),
    (r'^control-panel/$','control_panel'),
    (r'^operation/$','operation'),
    (r'^upload/$','upload'),
    (r'download/$','download'),
    (r'^move/$','move'),
    (r'^preview/$','preview'),
)
urlpatterns+=patterns('',
        (r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root':os.path.join(os.path.dirname(__file__),'site_media')}),
        (r'^download/(?P<path>.*)$','django.views.static.serve',
        {'document_root': os.path.join(os.path.dirname(__file__),'temp'),
        'show_indexes':True}),
        )
