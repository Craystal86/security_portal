from django.urls import path

from . import views

app_name = 'security_portal'

urlpatterns = [
    # 진원님 코드 추가하면서 주석처리
    # path('', views.index, name='index'),

    path('magazine_security/', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),

    # 진원님 코드 추가
    path('home/', views.home, name='home'),
    path('', views.home, name='home'),
    # 진원님 코드 종료
]