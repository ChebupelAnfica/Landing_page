from django.urls import path
from .views import StageOneView, StageTwoView

urlpatterns = [
    path('stage-one/', StageOneView.as_view(), name='stage-one'),
    path('stage-two/', StageTwoView.as_view(), name='stage-two'),
]
