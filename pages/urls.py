from .views import * 

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact'),
    path('services/', Services.as_view (), name='services'),
   ]