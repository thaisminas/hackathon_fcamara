from django.conf.urls import url
from . import views

app_name='users'

urlpatterns = [
  url('cadastro/', views.cadastro, name="cadastro")
]