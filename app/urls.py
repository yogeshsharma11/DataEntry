from django.urls import path
from . import views

urlpatterns=[
    path('',views.login_view,name='login'),
    path('register',views.register_view,name='register'),
    path('index',views.index,name='index'),
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('export-csv/', views.export_csv, name='export_csv'),
    path('delete-data/<int:data_id>/', views.delete_data, name='delete_data'),
    path('edit-data/<int:data_id>/', views.edit_data, name='edit_data'), 


]