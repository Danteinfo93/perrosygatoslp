from rest_framework import viewsets

from .models import Profile, Trainer, Ad, Adoption, Straying, Finding, Cross, Breed, Location
from .serializers import ProfileSerializer, TrainerSerializer, AdSerializer, AdoptionSerializer, StrayingSerializer, FindingSerializer, CrossSerializer, BreedSerializer, LocationSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

class AdoptionViewSet(viewsets.ModelViewSet):
    queryset = Adoption.objects.all()
    serializer_class = AdoptionSerializer

class StrayingViewSet(viewsets.ModelViewSet):
    queryset = Straying.objects.all()
    serializer_class = StrayingSerializer

class FindingViewSet(viewsets.ModelViewSet):
    queryset = Finding.objects.all()
    serializer_class = FindingSerializer

class CrossViewSet(viewsets.ModelViewSet):
    queryset = Cross.objects.all()
    serializer_class = CrossSerializer

class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer