from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.schools, name='schools'),
    path('<int:id>/teachers', views.teachers, name='teachers'),
    path('teachers', views.comment_save, name='comment_save'),
    path('teacher/<int:id>/comments', views.read_comment, name='read_comment'),
    path('<region>/<school_type_det>/schoolname', views.school_name, name='school_name'),
    path('teacher/<int:teacher_id>/<str:rating>/ratings', views.teacher_rating, name='teacher_rating'),
]