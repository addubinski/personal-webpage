from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from homepage.views import homepage, show_404, show_500, robots_txt
from projects.views import projects_home, view_project, project_search

handler404 = 'homepage.views.show_404'
handler500 = 'homepage.views.show_500'


def custom_404(request):
    return show_404(request, None)


urlpatterns = [
    path('', homepage, name='homepage'),
    path('projects/', projects_home, name='projects_home'),
    path('view_project/<int:project_id>/', view_project, name='view_project'),
    path('project_search/', project_search, name='project_search'),
    path('404/', custom_404),
    path('500/', show_500),
    path('robots.txt', robots_txt),
    path('admin/', admin.site.urls)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
