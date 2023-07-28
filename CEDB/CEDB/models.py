from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    employee_rank = models.CharField(max_length=100)
    employee_pay = models.CharField(max_length=100)
    years_of_experience = models.CharField(max_length=100)
    employee_picture = models.CharField(max_length=100)
    skill_level = models.CharField(max_length=100)

    def __str__(self):
        return self.employee_name


class Customer(models.Model):
    business_name  = models.CharField(max_length=100)
    manager = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    price_sqft = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.business_name
    

class Project(models.Model):
    description = models.CharField(max_length=100)
    start_date  = models.CharField(max_length=100)
    end_date  = models.CharField(max_length=100)
    project_manager = models.CharField(max_length=100)
    estimate = models.CharField(max_length=100)
    invoice  = models.CharField(max_length=100)
    total_cost = models.CharField(max_length=100)
    type_of_job = models.CharField(max_length=100)
    customer_id  = models.ForeignKey(Customer, db_column='customer_id', on_delete=models.CASCADE, related_name='projects')
    material_cost = models.CharField(max_length=100)
    labor_cost = models.CharField(max_length=100)
    employee_id = models.ManyToManyField(Employee, db_column='employee_id', related_name='projects')

    def __str__(self):
        return self.description

