from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100,write_only= True
)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_librarian', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user