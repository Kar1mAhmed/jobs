from django.urls import path

from . import views

app_name = "app1"


urlpatterns = [
    path("login/", views.login, name="login"),
    path("login-page/", views.login_page, name="login_page"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout, name="logout"),
    path("", views.home, name="home"),
    path("list-jobs/", views.list_jobs, name="list_jobs"),
    path("post-job-page/", views.post_job_page, name="post_job_page"),
    path("post-job/", views.post_job, name="post_job"),
    path("job-details/<int:pk>", views.job_details, name="job_details"),
    path("apply_page/<int:pk>", views.apply_page, name="apply_page"),
    path("apply/<int:pk>", views.apply, name="apply"),
    path(
        "delete-application/<int:pk>",
        views.delete_application,
        name="delete_application",
    ),
    path("posted-jobs/", views.posted_jobs, name="posted_jobs"),
    path("applied-jobs/", views.applied_jobs, name="applied_jobs"),
    path("edit-job-page/<int:pk>/", views.edit_job_page, name="edit_job_page"),
    path("delete-job/<int:pk>/", views.delete_job, name="delete_job"),
    path("edit-job/<int:pk>/", views.edit_job, name="edit_job"),
    path('favorite/<int:pk>/', views.favorite, name='favorite'),
    path('remove_favorite/<int:pk>/', views.remove_favorite, name='remove_favorite'),
    path('favorite_page/', views.favorite_page, name='favorite_page')
    
]
