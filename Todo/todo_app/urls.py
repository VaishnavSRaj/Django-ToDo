from django.urls import path
from todo_app import views

urlpatterns = [
    path('', views.todo, name='todo'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cvhome/', views.TaskListView.as_view(), name='cvhome'),
    path('cvdetail/<int:pk>/', views.TaskDetailView.as_view(), name='cvdetail'),
    path('cvupdate/<int:pk>/', views.TaskUpdateView.as_view(), name='cvupdate'),
    path('cvdelete/<int:pk>/', views.TaskDeleteView.as_view(), name='cvdelete')

]
