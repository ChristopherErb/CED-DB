from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('projects/', views.ProjectList.as_view(), name='project_list'),
    path('projects/<int:pk>', views.ProjectDetail.as_view(), name='project-detail'),

    path('employees/',views.EmployeeList.as_view(), name='employee_list'),
    path('employees/<int:pk>', views.EmployeeDetail.as_view(), name='employee-detail'),


    path('customers/', views.CustomerList.as_view(), name='customer_list'),
    path('customers/<int:pk>', views.CustomerDetail.as_view(), name='customer-detail')


]