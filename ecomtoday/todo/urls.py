from django.urls import path
from todo.views import *

urlpatterns = [
    path('record/create/', TodoCreateAPIView.as_view()),
    path('records/all/', TodoGetAPIView.as_view()),
    path('record/get/', TodoGetByUUID.as_view()),
    path('record/delete/<str:uuid>', TodoRemoveAPIView.as_view()),
    path('records/list/', TodoGetByDate.as_view()),
]