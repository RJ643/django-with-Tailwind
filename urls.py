from django.urls import include, path

Urlpatterns = [
	path('admin/', admin.site.urls),
	path('__reload__/', include('django_browser_reload.urls')),
	path('',include('blog.urls')),
]
