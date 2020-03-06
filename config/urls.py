from django.contrib import admin
from django.urls import include, path
from django.conf import settings

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
    path('', views.habits, name='habits'),
    path('habit_records/<int:pk>', views.habit_records, name='habit_records'),
    path('add_habit/', views.add_habit, name='add_habit'),
    path('add_record/', views.add_record, name='add_record'),
    path('habit_record/<int:pk>', views.habit_record, name='habit_record'),
    path('bar_chart/<int:pk>', views.bar_chart, name='bar_chart'),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns
