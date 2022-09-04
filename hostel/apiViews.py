from .models import *
from rest_framework.views import APIView
from rest_framework.serializers import ModelSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class LeaveRequestSerializer(ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = ['reason', 'start_date', 'end_date', 'visiting_place']
        read_only_fields = ['user']
    
    # automatically assign the user to the book
    def validate(self, attrs):
        attrs['user'] = self.context['request'].user
        return attrs

class ComplaintSerializer(ModelSerializer):
    class Meta:
        model = Complaint
        fields = ['complaint', 'expected_time']
        read_only_fields = ['user']
    
    # automatically assign the user to the book
    def validate(self, attrs):
        attrs['user'] = self.context['request'].user
        return attrs

class HealthReportSerializer(ModelSerializer):
    class Meta:
        model = HealthReport
        fields = ['reportee', 'description', 'date']
        read_only_fields = ['repoter']
    
    # automatically assign the user to the book
    def validate(self, attrs):
        attrs['user'] = self.context['request'].user
        return attrs

class RoomCleaningSerializer(ModelSerializer):
    class Meta:
        model = RoomCleaning
        fields = ['time']
        read_only_fields = ['user']
    
    # automatically assign the user to the book
    def validate(self, attrs):
        attrs['user'] = self.context['request'].user
        return attrs

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    # sign up new user
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user

class LeaveRequestViewSet(viewsets.ModelViewSet):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer

    def get_queryset(self):
        return LeaveRequest.objects.filter(user=self.request.user)

class ComplaintViewSet(viewsets.ModelViewSet):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer

    def get_queryset(self):
        return Complaint.objects.filter(user=self.request.user)

class HealthReportViewSet(viewsets.ModelViewSet):
    queryset = HealthReport.objects.all()
    serializer_class = HealthReportSerializer

    def get_queryset(self):
        return HealthReport.objects.filter(user=self.request.user)

class RoomCleaningViewSet(viewsets.ModelViewSet):
    queryset = RoomCleaning.objects.all()
    serializer_class = RoomCleaningSerializer

    def get_queryset(self):
        return RoomCleaning.objects.filter(user=self.request.user)

class APIUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# get logged in user's details
class CurrentUserView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
