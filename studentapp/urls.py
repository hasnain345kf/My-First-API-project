from django.urls import path
from .import views
urlpatterns = [
    path('students/',views.studentview.as_view(),name='student-list'),
]
