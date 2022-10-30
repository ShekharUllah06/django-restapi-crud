from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from mobile.serializers import MobileSerializer
from mobile.models import Phone

# This endpoint list all of the available phones from the database
class ListMobileAPIView(ListAPIView):
    queryset = Phone.objects.all()
    serializer_class = MobileSerializer

# This endpoint allows for creation of a phone
class CreateMobileAPIView(CreateAPIView):
    queryset = Phone.objects.all()
    serializer_class = MobileSerializer

# This endpoint allows for updating a specific phone by passing in the id of the phone to update
class UpdateMobileAPIView(UpdateAPIView):
    queryset = Phone.objects.all()
    serializer_class = MobileSerializer

# This endpoint allows for deletion of a specific phone from the database
class DeleteMobileAPIView(DestroyAPIView):
    queryset = Phone.objects.all()
    serializer_class = MobileSerializer
