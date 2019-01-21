
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from checkins import views


urlpatterns = [

    path('', views.home, name='home'),

    path('checkin/', views.checkin, name='checkin'),
    path('reserve/', views.reserve, name='reserve'),

    path('checkins/', views.checkins, name='checkins'),
    path('list/', views.attendee_list, name='list'),
    path('branchlist/<str:branch>', views.branch_list, name='branchlist'),

    path('slotform/', views.slot_form, name='slotform' ),

    path('upload/', views.upload_file, name='upload'),
    path('delete/<int:pk>/', views.delete_file, name='delete'),
    path('populate/<int:pk>/', views.populate, name='populate'),

    path('manage/', views.manage, name='manage'),

    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)