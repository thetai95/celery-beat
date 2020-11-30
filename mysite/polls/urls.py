from django.urls import path
from . import views

urlpatterns = [
    path('test_celery/', views.TestCelery.as_view(), name="test_celery"),
]
