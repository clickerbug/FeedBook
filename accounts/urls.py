from django.conf.urls import url

from . import views


urlpatterns = [
    url('signup/', views.SignUp.as_view(), name='signup'),
    url('add/', views.feedback_form, name='home'),

]
