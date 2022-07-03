from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.create_session, name="create_session"),
    path('detail/', views.vacant_sessions, name="vacant_sessions"),
    path('detail/', views.detail_sessions, name="detail_sessions"),
    path('update/<str:pk>', views.update_session, name="update_session"),
]
