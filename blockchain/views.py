from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from blockchain.serializers import BlockchainSerializer
from blockchain.models import Blockchain

class BlockchainList(ListAPIView):
    queryset = Blockchain.objects.all()
    serializer_class = BlockchainSerializer

class BlockchainCreate(CreateAPIView):
    queryset = Blockchain.objects.all()
    serializer_class = BlockchainSerializer

class BlockchainReset(ModelViewSet):
    queryset = Blockchain.objects.all()
    serializer_class = BlockchainSerializer

    @classmethod
    def reset(self, request, *args, **kwargs):
        return Response(Blockchain.objects.all().delete(), status=status.HTTP_205_RESET_CONTENT)
        