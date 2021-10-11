from django.contrib.auth.models import User

from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']
        extra_kwargs = dict(password={'write_only': True})

    def validate(self, attrs):
        if not attrs['password'] == attrs['password_confirm']:
            raise serializers.ValidationError('Password and password confirm do not match')

        return super().validate(attrs)

    def save(self, **kwargs):
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError(detail='Email already exists')

        user = User(email=self.validated_data['email'], username=self.validated_data['username'])
        user.set_password(self.validated_data['password'])
        user.save()

        return user
