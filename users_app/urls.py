
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", views.registerUser,name='register'),
    path("", views.loginUser,name='login'),
    path("logout/",views.logoutUser,name='logout'),
    path("account/<str:pk>/",views.account,name='account'),    
    path("edit_profile/<str:pk>/",views.update_profile,name="update_profile"),
    path("edit_password/<str:pk>/",views.change_password,name="change_password"),
    path("delete_account/<str:pk>/",views.delete_account,name="delete_account"),
    path("exercise/<str:pk>/",views.exercise,name="exercise_id"),
    path("exercise_solve/<str:pk>/<str:pk2>/",views.solve,name="solve"),
    path("exercises_solved/<str:pk>/",views.exercises_solved,name="solved"),
    path("exercise_type/<str:pk>/",views.list_of_exercises,name="exercise_type"),
]

urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)

