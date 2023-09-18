from django.db.models.query import QuerySet
from django.forms import fields
from rest_framework import serializers
from .models import Agent, Category, Lead, User


class UserSerializer(serializers.ModelSerializer):
    # email = serializers.SlugRelatedField(slug_field="email", read_only=True)
    class Meta:
        model=User
        fields = ('email',)


class AgentSerializers(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Agent
        fields = ('user', 'organization')



# Serializer class for my Lead model 

class LeadSerializers(serializers.ModelSerializer):
    # this allows me to serialize the cateogry names instead of the pk id
    agent = AgentSerializers()
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    # formatting for date created - m/d/y
    date_added = serializers.DateTimeField(format="%m-%d-%Y")
    # agent = serializers.SlugRelatedField(slug_field="user", read_only=True)
    class Meta:
        model = Lead
        fields = ('first_name', 'last_name', 'age', 'agent',
        'organization', 'description', 'date_added', 
        'phone_number', 'email', 'category')






# class LeadSerializers(serializers.ModelSerializer):

#     class Meta:
#         model = Lead
#         fields = ('first_name', 'last_name', 'age', 'agent',
#         'organization', 'category', 'description', 'date_added', 
#         'phone_number', 'email')



# class AgentSerializers(serializers.ModelSerializer):

#     class Meta:
#         model = Agent
#         fields = ('user', 'organization')


class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'organization')