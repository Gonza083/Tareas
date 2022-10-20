
from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.index, name="index"),
    path('signup/', views.signup, name ="signup"),
    path('task/', views.task, name="task"),
    path('task_completed/',views.task_completed, name="task_completed"),    
    path('logout/', views.signout, name="logout"),
    
    path('signin/', views.signin, name='signin'),
    path('task/<int:task_id>', views.task_detail, name= 'task_detail' ),
    path('task/create', views.create_task, name= 'create_task' ),
    path('task/<int:task_id>/complete', views.complete_task, name= 'complete_task' ),
    path('task/<int:task_id>/detail', views.task_detail, name= 'task_detail' ),
    path('task/<int:task_id>/delete', views.delete_task, name= 'delete_task' ),
]