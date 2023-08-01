from rest_framework import serializers
from .models import Employee, Customer, Project




class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    projects = serializers.HyperlinkedRelatedField(
        view_name='project-detail',
        many=True,
        read_only=True
    )

    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(),
    )

    class Meta:
        model = Project
        fields = '__all__'



class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    employees = serializers.HyperlinkedRelatedField(
        view_name = 'customer_detail',
        many=True,
        read_only=True
    )

    employee_url = serializers.ModelSerializer.serializer_url_field(
        view_name='employee-detail'
    )


    class Meta:
        model = Employee
        fields = '__all__'


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    # customers = serializers.HyperlinkedRelatedField(
    #     view_name = 'customer-detail',
    #     many=True,
    #     read_only=True
    # )

    class Meta:
        model = Customer
        fields = ('id', 'url','business_name','manager','address','price_sqft','description')


