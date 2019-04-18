from django.contrib.auth.models import User
from rest_framework import serializers
from core.models import Human, Child


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class HumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = ('name', 'content', 'data', 'childs')

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ('name', 'content', 'human')