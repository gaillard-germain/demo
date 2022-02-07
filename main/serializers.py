from rest_framework import serializers
from .models import User, Profile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', )


class ProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ('user',
                  'hometown',
                  'age',
                  'gender')

    def create(self, validated_data):
        temp_user = validated_data.pop('user')
        user = User.objects.create(username=temp_user['username'])
        user.save()
        validated_data['user'] = user
        profile = super(ProfileSerializer, self).create(validated_data)
        profile.save()

        return profile
