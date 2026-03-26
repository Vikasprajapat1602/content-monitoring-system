from django.shortcuts import render
from rest_framework import generics
from .models import Keyword, Flag
from .serializers import KeywordSerializer, FlagSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .services import load_content, run_matching, generate_flags, run_scan
from django.utils.timezone import now






# Create or List API
class KeywordListCreateView(generics.ListCreateAPIView):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer


class LoadContentView(APIView):
    def post(self, request):
        load_content()
        return Response({"message": "Content loaded successfully"})
    


class MatchTestView(APIView):
    def get(self, request):
        data = run_matching()
        return Response(data)
    

class GenerateFlagView(APIView):
    def post(self, request):
        flags = generate_flags()
        return Response({
            "message": "Flags generated",
            "flag_ids": flags
        })
    


class ScanView(APIView):
    def post(self, request):
        result = run_scan()
        return Response(result)
    


# GET all flags
class FlagListView(generics.ListAPIView):
    queryset = Flag.objects.all()
    serializer_class = FlagSerializer


# PATCH (update status)
class FlagUpdateView(generics.UpdateAPIView):
    queryset = Flag.objects.all()
    serializer_class = FlagSerializer

    def perform_update(self, serializer):
        instance = serializer.save()

        # when reviewer update
        if instance.status == "irrelevant":
            instance.last_reviewed_at = now()
            instance.save()