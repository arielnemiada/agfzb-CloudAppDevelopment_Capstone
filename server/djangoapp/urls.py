from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL
    # path for about view
    path(route='', view=views.home, name='Home'),

    # path for about view
    path(route='about-us', view=views.about, name='About Us'),

    # path for contact us view
    path(route='contact-us', view=views.contact, name='Contact Us'),

    # path for registration
    path(route='registration', view=views.registration_request, name='Registration'),

    # path for login
    path(route='login', view=views.login_request, name='Login'),

    # path for logout

    path(route='', view=views.get_dealerships, name='index'),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)