from django.urls import path
from .views import HomeView, AddDonateView, AddStudentView, LandingView, StudentView

urlpatterns = [
    path('', LandingView.as_view(), name = 'landing'),
    path('home', HomeView.as_view(), name = 'home'),
    path('add_donate/', AddDonateView.as_view(), name = 'add_donate'),
    path('add_student/', AddStudentView.as_view(), name = 'add_student'),
    path('student/', StudentView.as_view(), name = 'student'),
]
