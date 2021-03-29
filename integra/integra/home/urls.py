from django.urls import path
from .views import HomeView, DonatedView, AddDonateView, ProfileRegisterView, AddStudentView, LandingView, StudentView, SchoolView, LocalSchoolView, MyDonationsView

urlpatterns = [
    path('', LandingView.as_view(), name = 'landing'),
    path('home', HomeView.as_view(), name = 'home'),
    #path('add_donate/<int:pk>/', AddDonateView.as_view(), name = 'add_donate'),
    path('add_donate/', AddDonateView.as_view(), name = 'add_donate'),
    path('add_student/', AddStudentView.as_view(), name = 'add_student'),
    path('student/', StudentView.as_view(), name = 'student'),
    path('school/<str:schl>/', SchoolView, name = 'school'),
    path('local/<str:stt>/<str:city>', LocalSchoolView, name = 'local_school'),
    path('my_donations/', MyDonationsView.as_view(), name = 'my_donations'),
    path('profile_register/', ProfileRegisterView.as_view(), name = 'profile_register'),
    path('donated/', DonatedView.as_view(), name = 'donated'),
]
