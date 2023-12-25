from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='home'),
    path('hosts/', hosts, name='hosts'),
    path('animals/', animals, name='animals'),
    path('diseasis/', diseasis, name='diseases'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegistrationView.as_view(), name='register'),

    path('hosts/select/', hosts_select, name='hosts_select'),
    path('hosts/update/', hosts_update, name='hosts_update'),
    path('hosts/insert/', hosts_insert, name='hosts_insert'),
    path('hosts/delete/', hosts_delete, name='hosts_delete'),
    path('hosts/word/', hword, name='howrd'),
    path('hosts/excel/', hexcel, name='hexcel'),
    path('hosts/pdf/', hpdf, name='hpdf'),

    path('animals/select/', animals_select, name='animals_select'),
    path('animals/update/', animals_update, name='animals_update'),
    path('animals/insert/', animals_insert, name='animals_insert'),
    path('animals/delete/', animals_delete, name='animals_delete'),
    path('animals/word/', aword, name='aowrd'),
    path('animals/excel/', aexcel, name='aexcel'),
    path('animals/pdf/', apdf, name='apdf'),

    path('diseasis/select/', diseases_select, name='diseases_select'),
    path('diseasis/update/', diseases_update, name='diseases_update'),
    path('diseasis/insert/', diseases_insert, name='diseases_insert'),
    path('diseasis/delete/', diseases_delete, name='diseases_delete'),
    path('diseasis/word/', dword, name='dowrd'),
    path('diseasis/excel/', dexcel, name='dexcel'),
    path('diseasis/pdf/', dpdf, name='dpdf'),
]