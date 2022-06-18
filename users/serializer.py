from .models import Users
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    email = serializers.CharField()

    class Meta:
        model = Users
        fields = ('id', 'username', 'email', 'password', 'password2')
        extra_kwargs = {'username': {'required': True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "les deux mots de passe ne sont pas identique"})
        return attrs

    def validate_email(self, value):
        if Users.objects.filter(email=value).exists():
            raise serializers.ValidationError('"Un utilisateur avec cet email existe déjà."')
        return value

    def create(self, validated_data):
        user = Users.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
