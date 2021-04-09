from django.urls import path
from .views import HomeView, AddItemSelection, DonatedView, UpdateItemSelection, PayementView,AddDonateView, ProfileRegisterView, AddStudentView, LandingView, StudentView, SchoolView, LocalSchoolView, MyDonationsView, DeliveredDonateView, ColectedDonateView, LocalStateView, FindSchoolView, Createlist

urlpatterns = [
    path('', LandingView.as_view(), name = 'landing'),
    path('home', HomeView.as_view(), name = 'home'),
    path('add_donate/<int:pk>/', AddDonateView.as_view(), name = 'add_donate'),
    #path('add_donate/', AddDonateView.as_view(), name = 'add_donate'),
    path('add_student/', AddStudentView.as_view(), name = 'add_student'),
    path('student/', StudentView.as_view(), name = 'student'),
    path('school/<str:schl>/', SchoolView, name = 'school'),
    path('local/<str:stt>/<str:city>', LocalSchoolView, name = 'local_school'),
    path('my_donations/', MyDonationsView.as_view(), name = 'my_donations'),
    path('profile_register/', ProfileRegisterView.as_view(), name = 'profile_register'),
    path('donated/', DonatedView.as_view(), name = 'donated'),
    #path('add_list/<int:pk>', AddListView.as_view(), name = 'add_list'),
    path('add_list/<int:pk>', Createlist, name = 'add_list'),
    path('edit_list/<int:pk>', UpdateItemSelection.as_view(), name = 'edit_list'),
    path('delivered_donations/<int:pk>', DeliveredDonateView.as_view(), name = 'delivered_donations'),
    path('colected_donation/<int:pk>', ColectedDonateView.as_view(), name = 'colected_donation'),
    path('payement/<int:pk>', PayementView.as_view(), name = 'payement'),
    path('local_state/<str:stt>/', LocalStateView, name = 'local_state'),
    path('find_school/', FindSchoolView, name = 'find_school'),
    path('add_item/<int:pk>', AddItemSelection.as_view(), name = 'add_item'),
]
