from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    def validate_email(self, value: str) -> str:
        
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                'This field must be unique.')
        return value

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        password = validated_data.pop('password', None)

        if password:
            instance.set_password(password)
        
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        
        return instance
    
    class Meta:
        model = User
        fields = 'id', 'username', 'full_name', 'artistic_name', 'email', 'password'
        read_only_fields = ['id']
        extra_kwargs = {'password': {'write_only': True},
                        'username': {'validators': [UniqueValidator(queryset=User.objects.all(), message="A user with that username already exists.")]}}