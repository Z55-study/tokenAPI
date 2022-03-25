from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import TokenT
from .serializers import TokenTSerializer

from .services import generate_str
from .total_supply import totalSupply


class TotalAPIView(APIView):

    def get(self, request):
        return Response({'result': totalSupply})


class TokenAPIView(APIView):
    def post(self, request):
        ex = generate_str(20)
        post_new = TokenT.objects.create(
            owner=request.data['owner'],
            media_url=request.data['media_url'],
            unique_hash=ex
        )
        return Response({'tokensT': model_to_dict(post_new)})


class TokenTPagination(PageNumberPagination):
    page_size = 200
    page_size_query_param = 'page_size'
    max_page_size = 500


class TokenTAPIList(generics.ListAPIView):
    queryset = TokenT.objects.all()
    serializer_class = TokenTSerializer
    pagination_class = TokenTPagination

# class TokenTAPICreate(generics.CreateAPIView):
#     queryset = TokenT.objects.all()
#     serializer_class = TokenCreateSerializer
#
#
# class TokenTAPIListContract(generics.ListAPIView):
#     queryset = TokenT.objects.all()
#     serializer_class = TokenTSerializer
