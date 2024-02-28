from django.urls import path
from tasks.views import*

urlpatterns = [
    path("", index, name="task_list"),
    path("update/<str:pk>/", UpdateTask, name="update_task"),
    path("complete/<str:pk>/", CompleteTask, name="complete_task"),
    path("delete/<str:pk>/", DeleteTask, name="delete_task"),
]