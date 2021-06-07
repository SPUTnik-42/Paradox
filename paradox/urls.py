from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("user-profile", views.user_profile, name="user-profile"),
    path("question", views.question_page, name="question-page"),
    path("hint", views.hint_page, name="hint-page"),
    path("leaderboard", views.leaderboard_page, name="leaderboard-page"),
    path("log",views.log_page, name="log-page"),
    path("disqualification", views.disqualification_page, name="disqualification-page"),
    path("disqualify/<int:user_id>", views.disqualify, name="disqualify"),
    path("undisqualify/<int:user_id>", views.un_disqualify, name="un-disqualify")
]