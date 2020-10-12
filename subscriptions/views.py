from django.shortcuts import render

# Create your views here.
from .models import Subscription
from .serializers import SubscriptionSerializer
from rest_framework import generics


class SubscriptionList(generics.ListCreateAPIView):
    
    queryset = Subscription.objects.all()
    print(queryset)
    # class-based generic API views
    serializer_class = SubscriptionSerializer


class SubscriptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer