from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import Profile
from .serializers import ProfileSerializer


class UserList(APIView):
    """ Lists all users through several filters """

    def get(self, request, format=None):
        profiles = Profile.objects.all()

        hometown = request.GET.get('hometown', None)
        age_min = request.GET.get('age_min', None)
        age_max = request.GET.get('age_max', None)
        gender = request.GET.get('gender', None)

        if hometown:
            profiles = profiles.filter(hometown__icontains=hometown)
        if age_min:
            profiles = profiles.filter(age__gte=age_min)
        if age_max:
            profiles = profiles.filter(age__lte=age_max)
        if gender:
            profiles = profiles.filter(gender=gender)

        profile_serializer = ProfileSerializer(profiles, many=True)

        return Response(profile_serializer.data)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
