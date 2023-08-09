from django.contrib import admin
from django.urls import path 
from myapp import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomeView.as_view()),
    path('candidate.html<int:pk>/',views.CandidateView,name="candidate_view"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


