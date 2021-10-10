from os import name
from django.urls import path
from . import views

urlpatterns = [
    # Register, Login, dashboard, logout
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('user_dashboard', views.user_dashboard, name='user_dashboard'),
    path('logout', views.logout, name='logout'),
    # Email verification
    path('token', views.token_send,  name='token_send'),
    path('verify/<auth_token>', views.verify, name='verify'),
    path('error', views.error, name='error'),
    # Reset Password
    path('reset_password_send_email', views.reset_pass_send_email, name='reset_pass_send_email'),
    path('reset_password/<get_token>', views.reset_password, name='reset_password'),
    path('reset_password_form/<get_token>', views.reset_password_form, name="reset_password_form"),
    # All info about schools, teachers,subjects and comments
    path('schools_info', views.schools, name='schools_info'),
    path('teachers', views.teachers, name='teachers'),
    path('admin/subjects', views.subjects,  name='admin_subjects'),
    path('comments/<int:id>', views.comments,  name='comments'),
    # All actions over comments
    path('user/comments/<int:id>', views.comments,  name='user_comments'),
    path('admin/comments/delete/<int:id>', views.comments_delete,  name='comments_delete'),
    path('admin/comments/hide/<int:id>', views.comments_hide_unhide,  name='comments_hide_unhide'),
    # All actions over applies
    path('applies/<str:apply_type>', views.applies,  name='applies'),
    path('apply/delete/<int:id>', views.apply_delete,  name='apply_delete'),
    path('applies/receive_apply/<int:id>', views.receive_apply, name="receive_apply"),
    path('applies/reject_apply/<int:id>', views.reject_apply, name="reject_apply"),
    path('applies/apply_full_info/<int:id>', views.apply_full_info, name="apply_full_info"),
    path('making_apply/<int:id>', views.making_apply,  name='making_apply'),
    # All actions over profile settings
    path('profile', views.profile, name ='profile'),
    path('profile_save/<int:user_id>', views.profile_save, name ='profile_save'),
    path('account_delete/<int:id>', views.account_delete, name ='account_delete'),
    path('profile_photo_delete/<int:profile_id>', views.profile_photo_delete, name ='profile_photo_delete'),
]
